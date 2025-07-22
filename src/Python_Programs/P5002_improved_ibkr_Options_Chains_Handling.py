#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Professional-Grade IBKR Options Chain Handler

This implementation demonstrates production-ready patterns for interfacing with
Interactive Brokers' WebAPI to systematically retrieve and process options chain data.
Built with enterprise-level error handling, type safety, and maintainability principles.

Requirements:
- Python 3.13+
- IBKR Client Portal Gateway running on localhost:5001
- Active market data permissions for target symbols

Architecture:
- Modular design with single-responsibility functions
- Comprehensive error handling with custom exceptions
- Type hints for enhanced IDE support and code clarity
- Context managers for resource safety
- Progress tracking for long-running operations

Author: Pete W.
License: MIT License
Copyright (c) 2025 Pete W.
"""

import requests
import urllib3
import csv
import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Self
import time
import random

# Configure logging for production monitoring
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Suppress SSL warnings for localhost development
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@dataclass
class IBKRConfig:
    """Configuration settings for IBKR options chain processing."""
    base_url: str = "https://localhost:5001"
    timeout: int = 30
    symbol: str = "AAPL"
    exchange: str = "NASDAQ"
    price_range: float = 15.0
    option_type: str = "P"  # P for puts, C for calls
    
    def __post_init__(self):
        """Validate configuration after initialization."""
        if self.timeout <= 0:
            raise ValueError("Timeout must be positive")
        if self.price_range <= 0:
            raise ValueError("Price range must be positive")
        if self.option_type not in ("P", "C", "PUT", "CALL"):
            raise ValueError("Option type must be P, C, PUT, or CALL")


class IBKRAPIError(Exception):
    """Custom exception for IBKR API-related errors"""
    pass


class DataValidationError(Exception):
    """Custom exception for data validation failures"""
    pass


@dataclass
class OptionsContract:
    """Structured representation of an options contract"""
    conid: str
    symbol: str
    strike: float
    maturity_date: str
    contract_type: str = "PUT"
    
    def __post_init__(self):
        """Validate contract data after initialization"""
        if not self.conid:
            raise DataValidationError("Contract ID cannot be empty")
        if self.strike <= 0:
            raise DataValidationError("Strike price must be positive")


class IBKROptionsChainHandler:
    """
    Professional-grade handler for IBKR options chain operations.
    
    This class encapsulates all interactions with the IBKR WebAPI,
    providing robust error handling, data validation, and progress tracking.
    """
    
    def __init__(self, base_url: str = "https://localhost:5001", timeout: int = 30):
        """
        Initialize the options chain handler.
        
        Args:
            base_url: IBKR Client Portal Gateway URL
            timeout: Request timeout in seconds
        """
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.verify = False  # For localhost development only
        self.performance_monitor = PerformanceMonitor()
    
    def configure_timeout(self, timeout: int) -> Self:
        """Configure request timeout with method chaining support."""
        self.timeout = timeout
        return self
    
    def configure_base_url(self, base_url: str) -> Self:
        """Configure base URL with method chaining support."""
        self.base_url = base_url
        return self
    
    @classmethod
    def from_config(cls, config: IBKRConfig) -> Self:
        """
        Create handler instance from configuration object.
        
        Args:
            config: IBKRConfig instance with settings
            
        Returns:
            Configured IBKROptionsChainHandler instance
        """
        return cls(base_url=config.base_url, timeout=config.timeout)
    
    def _retry_with_backoff(self, func, max_attempts: int = 3, base_delay: float = 1.0):
        """
        Retry a function with exponential backoff.
        
        Args:
            func: Function to retry
            max_attempts: Maximum number of retry attempts
            base_delay: Base delay in seconds
            
        Returns:
            Function result if successful
            
        Raises:
            Last exception if all attempts fail
        """
        last_exception = None
        
        for attempt in range(max_attempts):
            try:
                return func()
            except (requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
                last_exception = e
                if attempt < max_attempts - 1:  # Don't sleep on last attempt
                    delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
                    logger.warning(f"Request failed (attempt {attempt + 1}/{max_attempts}), retrying in {delay:.1f}s: {str(e)}")
                    time.sleep(delay)
                else:
                    logger.error(f"All {max_attempts} attempts failed")
            except Exception as e:
                # For non-retryable exceptions, fail immediately
                logger.error(f"Non-retryable error: {str(e)}")
                raise e
                
        raise last_exception
        
    def _make_request(self, endpoint: str, params: dict | None = None) -> dict:
        """
        Make authenticated request to IBKR API with comprehensive error handling.
        
        Args:
            endpoint: API endpoint path
            params: Query parameters
            
        Returns:
            JSON response data
            
        Raises:
            IBKRAPIError: For API-related failures
        """
        url = f"{self.base_url}{endpoint}"
        start_time = time.time()
        success = False
        
        def _request():
            response = self.session.get(
                url, 
                params=params or {}, 
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        
        try:
            data = self._retry_with_backoff(_request)
            success = True
            logger.debug(f"API request successful: {endpoint}")
            return data
            
        except requests.exceptions.RequestException as e:
            error_msg = f"API request failed for {endpoint}: {str(e)}"
            logger.error(error_msg)
            raise IBKRAPIError(error_msg) from e
        except ValueError as e:
            error_msg = f"Invalid JSON response from {endpoint}: {str(e)}"
            logger.error(error_msg)
            raise IBKRAPIError(error_msg) from e
        finally:
            duration = time.time() - start_time
            self.performance_monitor.record_request(success, duration)
    
    def find_security_contract(self, symbol: str, exchange: str) -> tuple[str, list[str]] | None:
        """
        Search for security definition and extract contract details.
        
        This method queries the IBKR security definition endpoint to locate
        the primary contract for a given symbol and exchange combination.
        
        Args:
            symbol: Stock ticker symbol (e.g., 'AAPL')
            exchange: Primary listing exchange (e.g., 'NASDAQ')
            
        Returns:
            Tuple of (contract_id, available_months) or None if not found
        """
        logger.info(f"Searching for {symbol} on {exchange}")
        
        try:
            data = self._make_request(
                "/v1/api/iserver/secdef/search",
                {"symbol": symbol}
            )
            
            if not data:
                logger.warning(f"No contracts found for symbol {symbol}")
                return None
                
            # Find matching exchange contract
            for contract in data:
                if contract.get("description") == exchange:
                    contract_id = contract.get("conid")
                    
                    # Extract options expiration months
                    months = self._extract_option_months(contract)
                    
                    if contract_id and months:
                        logger.info(f"Found contract {contract_id} with {len(months)} expiration months")
                        return str(contract_id), months
                        
            logger.warning(f"No options contract found for {symbol} on {exchange}")
            return None
            
        except IBKRAPIError:
            logger.error(f"Failed to search for security {symbol}")
            return None
    
    def _extract_option_months(self, contract: dict) -> list[str]:
        """Extract and validate options expiration months from contract data."""
        months = []
        
        sections = contract.get("sections", [])
        for section in sections:
            if section.get("secType") == "OPT":
                months_str = section.get("months", "")
                if months_str:
                    months = [m.strip() for m in months_str.split(";") if m.strip()]
                    break
                    
        return months
    
    def get_current_price(self, contract_id: str) -> float | None:
        """
        Retrieve current market price for underlying security.
        
        This method implements the required double-request pattern for IBKR
        market data endpoints, handling the preflight request automatically.
        
        Args:
            contract_id: Unique contract identifier
            
        Returns:
            Current last price or None if unavailable
        """
        logger.info(f"Fetching current price for contract {contract_id}")
        
        endpoint = "/v1/api/iserver/marketdata/snapshot"
        params = {"conids": contract_id, "fields": "31"}  # Field 31 = Last Price
        
        try:
            # First request (preflight for market data initialization)
            self._make_request(endpoint, params)
            
            # Brief pause to allow data population
            time.sleep(0.5)
            
            # Second request for actual data
            data = self._make_request(endpoint, params)
            
            if data and len(data) > 0 and "31" in data[0]:
                price = float(data[0]["31"])
                logger.info(f"Current {price=:.2f}")  # Enhanced f-string
                return price
            else:
                logger.warning("No price data available")
                return None
                
        except (ValueError, KeyError, IndexError) as e:
            logger.error(f"Price data parsing error: {str(e)}")
            return None
    
    def get_strike_prices(
        self, 
        contract_id: str, 
        month: str, 
        current_price: float,
        price_range: float = 10.0
    ) -> list[float]:
        """
        Retrieve filtered strike prices near current market price.
        
        This method fetches available strike prices and filters them to include
        only those within a specified range of the current market price,
        reducing data volume and focusing on tradeable contracts.
        
        Args:
            contract_id: Underlying security contract ID
            month: Target expiration month
            current_price: Current market price for filtering
            price_range: Price range above/below current price to include
            
        Returns:
            List of strike prices within the specified range
        """
        logger.info(f"Fetching strikes for month {month}, price range: ${current_price:.2f} ± ${price_range}")
        
        try:
            data = self._make_request(
                "/v1/api/iserver/secdef/strikes",
                {
                    "conid": contract_id,
                    "secType": "OPT",
                    "month": month
                }
            )
            
            # Extract put strikes (calls typically match, but puts are more reliable)
            raw_strikes = data.get("put", [])
            
            # Filter strikes within price range
            filtered_strikes = []
            lower_bound = current_price - price_range
            upper_bound = current_price + price_range
            
            for strike in raw_strikes:
                if isinstance(strike, (int, float)):
                    strike_price = float(strike)
                    if lower_bound <= strike_price <= upper_bound:
                        filtered_strikes.append(strike_price)
            
            logger.info(f"Found {len(filtered_strikes)} strikes in range: {filtered_strikes}")
            return sorted(filtered_strikes)
            
        except IBKRAPIError:
            logger.error(f"Failed to retrieve strikes for contract {contract_id}")
            return []
    
    def get_contract_details(
        self, 
        contract_id: str, 
        month: str, 
        strike: float,
        option_type: str = "P"
    ) -> list[OptionsContract]:
        """
        Retrieve detailed contract specifications for specific strike.
        
        This method queries the contract info endpoint to get comprehensive
        details about all available expiration dates within the specified month.
        
        Args:
            contract_id: Underlying security contract ID
            month: Target expiration month
            strike: Strike price
            option_type: Option type ('P' for puts, 'C' for calls)
            
        Returns:
            List of OptionsContract objects with full specifications
        """
        logger.debug(f"Fetching contract details: strike ${strike}, type {option_type}")
        
        try:
            data = self._make_request(
                "/v1/api/iserver/secdef/info",
                {
                    "conid": contract_id,
                    "month": month,
                    "strike": str(strike),
                    "secType": "OPT",
                    "right": option_type
                }
            )
            
            contracts = []
            for contract_data in data:
                try:
                    # Use pattern matching for option type processing
                    match option_type:
                        case "P" | "PUT":
                            contract_type = "PUT"
                        case "C" | "CALL":
                            contract_type = "CALL"
                        case _:
                            contract_type = "PUT"  # Default fallback
                    
                    contract = OptionsContract(
                        conid=str(contract_data.get("conid", "")),
                        symbol=contract_data.get("symbol", ""),
                        strike=float(contract_data.get("strike", 0)),
                        maturity_date=contract_data.get("maturityDate", ""),
                        contract_type=contract_type
                    )
                    contracts.append(contract)
                except (ValueError, DataValidationError) as e:
                    logger.warning(f"Skipping invalid contract data: {str(e)}")
                    continue
            
            logger.debug(f"Retrieved {len(contracts)} valid contracts for strike ${strike}")
            return contracts
            
        except IBKRAPIError:
            logger.error(f"Failed to retrieve contract details for strike ${strike}")
            return []
    
    def get_contract_details_batch(
        self,
        contract_id: str,
        month: str,
        strikes: list[float],
        option_type: str = "P",
        progress_callback: callable = None
    ) -> dict[float, list[OptionsContract]]:
        """
        Retrieve contract details for multiple strikes with progress tracking.
        
        Args:
            contract_id: Underlying security contract ID
            month: Target expiration month
            strikes: List of strike prices to process
            option_type: Option type ('P' for puts, 'C' for calls)
            progress_callback: Optional callback function for progress updates
            
        Returns:
            Dictionary mapping strikes to contract lists
        """
        logger.info(f"Processing {len(strikes)} strikes in batch")
        results = {}
        
        for i, strike in enumerate(strikes, 1):
            if progress_callback:
                progress_callback(i, len(strikes), strike)
            
            contracts = self.get_contract_details(contract_id, month, strike, option_type)
            if contracts:
                results[strike] = contracts
            
            # Small delay between requests to be respectful to API
            if i < len(strikes):  # Don't sleep after last request
                time.sleep(0.1)
        
        logger.info(f"Batch processing complete: {len(results)}/{len(strikes)} strikes successful")
        return results
    
    def export_to_csv(
        self, 
        contracts_by_strike: dict[float, list[OptionsContract]], 
        filename: str | None = None
    ) -> bool:
        """
        Export contract data to CSV with professional formatting.
        
        This method creates a well-structured CSV file with comprehensive
        contract information, suitable for further analysis or trading systems.
        
        Args:
            contracts_by_strike: Dictionary mapping strikes to contract lists
            filename: Output filename (auto-generated if None)
            
        Returns:
            True if export successful, False otherwise
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"options_contracts_{timestamp}.csv"
        
        logger.info(f"Exporting {len(contracts_by_strike)} strike groups to {filename}")
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = [
                    'contract_id', 'symbol', 'strike_price', 
                    'maturity_date', 'contract_type', 'export_timestamp'
                ]
                
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                
                export_time = datetime.now().isoformat()
                contracts_written = 0
                
                for strike_price in sorted(contracts_by_strike.keys()):
                    contracts = contracts_by_strike[strike_price]
                    
                    for contract in contracts:
                        writer.writerow({
                            'contract_id': contract.conid,
                            'symbol': contract.symbol,
                            'strike_price': f"{contract.strike:.2f}",
                            'maturity_date': contract.maturity_date,
                            'contract_type': contract.contract_type,
                            'export_timestamp': export_time
                        })
                        contracts_written += 1
                
                logger.info(f"Successfully exported {contracts_written} contracts to {filename}")
                return True
                
        except IOError as e:
            logger.error(f"Failed to write CSV file: {str(e)}")
            return False


class PerformanceMonitor:
    """Simple performance monitoring for API operations."""
    
    def __init__(self):
        self.stats = {
            'total_requests': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'total_time': 0.0
        }
    
    def record_request(self, success: bool, duration: float):
        """Record request statistics."""
        self.stats['total_requests'] += 1
        self.stats['total_time'] += duration
        
        if success:
            self.stats['successful_requests'] += 1
        else:
            self.stats['failed_requests'] += 1
    
    def get_summary(self) -> dict:
        """Get performance summary."""
        if self.stats['total_requests'] > 0:
            avg_time = self.stats['total_time'] / self.stats['total_requests']
            success_rate = self.stats['successful_requests'] / self.stats['total_requests'] * 100
        else:
            avg_time = 0.0
            success_rate = 0.0
            
        return {
            'total_requests': self.stats['total_requests'],
            'success_rate': f"{success_rate:.1f}%",
            'average_response_time': f"{avg_time:.3f}s",
            'total_time': f"{self.stats['total_time']:.2f}s"
        }


def main():
    """
    Main execution function demonstrating enterprise-grade options chain processing.
    
    This function orchestrates the complete workflow from symbol search through
    data export, with comprehensive error handling and progress tracking.
    """
    # Configuration using new IBKRConfig dataclass
    config = IBKRConfig(
        symbol="AAPL",
        exchange="NASDAQ",
        price_range=15.0,
        timeout=45,  # Longer timeout for production
        base_url="https://localhost:5001"
    )
    
    print("🚀 IBKR Professional Options Chain Handler")
    print("=" * 50)
    print(f"📊 Configuration: {config.symbol} on {config.exchange}")
    print(f"🎯 Price range: ±${config.price_range}")
    
    # Initialize handler using configuration
    handler = IBKROptionsChainHandler.from_config(config)
    
    try:
        # Step 1: Find security contract
        print(f"🔍 Searching for {config.symbol} on {config.exchange}...")
        result = handler.find_security_contract(config.symbol, config.exchange)
        
        if not result:
            print(f"❌ Could not locate {config.symbol} on {config.exchange}. Exiting.")
            return 1
            
        contract_id, available_months = result
        print(f"✅ Found {contract_id=}")  # Enhanced f-string
        print(f"📅 Available months: {', '.join(available_months)}")
        
        # Step 2: Get current price
        print(f"\n📊 Fetching current market price...")
        current_price = handler.get_current_price(contract_id)
        
        if current_price is None:
            print("❌ Could not retrieve current price. Exiting.")
            return 1
            
        print(f"💰 Current {current_price=:.2f}")  # Enhanced f-string
        
        # Step 3: Select target month (front month)
        target_month = available_months[0]
        print(f"🎯 Target month: {target_month}")
        
        # Step 4: Get filtered strike prices
        print(f"\n🔢 Fetching strike prices within ${config.price_range} of current price...")
        strikes = handler.get_strike_prices(
            contract_id, 
            target_month, 
            current_price, 
            config.price_range
        )
        
        if not strikes:
            print("❌ No suitable strike prices found. Exiting.")
            return 1
            
        print(f"✅ Found {len(strikes)} relevant strikes: {[f'${s:.0f}' for s in strikes]}")
        
        # Step 5: Retrieve contract details using batch processing
        print(f"\n📋 Retrieving detailed contract information...")
        
        def progress_callback(current: int, total: int, strike: float):
            """Progress callback for batch processing."""
            print(f"  [{current}/{total}] Processing {strike=:.0f}...")
        
        contracts_by_strike = handler.get_contract_details_batch(
            contract_id,
            target_month,
            strikes,
            config.option_type,
            progress_callback
        )
        
        # Display results
        for strike, contracts in contracts_by_strike.items():
            match len(contracts):  # Pattern matching for different outcomes
                case 0:
                    print(f"    ⚠️  No contracts found for ${strike:.0f}")
                case 1:
                    print(f"    ✅ Found 1 contract for ${strike:.0f}")
                case n:
                    print(f"    ✅ Found {n} contracts for ${strike:.0f}")
        
        # Step 6: Export results
        if contracts_by_strike:
            total_contracts = sum(len(contracts) for contracts in contracts_by_strike.values())
            print(f"\n💾 Exporting {total_contracts} contracts across {len(contracts_by_strike)} strikes...")
            
            success = handler.export_to_csv(contracts_by_strike)
            if success:
                print("✅ Export completed successfully!")
                print("📄 Data ready for trading system integration")
            else:
                print("❌ Export failed")
                return 1
        else:
            print("❌ No contract data to export")
            return 1
            
        print(f"\n🎉 Options chain processing completed successfully!")
        
        # Display performance statistics
        perf_stats = handler.performance_monitor.get_summary()
        print(f"\n📈 Performance Summary:")
        print(f"   • Total API requests: {perf_stats['total_requests']}")
        print(f"   • Success rate: {perf_stats['success_rate']}")
        print(f"   • Average response time: {perf_stats['average_response_time']}")
        print(f"   • Total processing time: {perf_stats['total_time']}")
        
        return 0
        
    except KeyboardInterrupt:
        print("\n⏹️  Operation cancelled by user")
        return 1
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        print(f"❌ Unexpected error occurred: {str(e)}")
        return 1


if __name__ == "__main__":
    exit(main())
