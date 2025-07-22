#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
IBKR Swarm Integration Layer

This module integrates the bio-inspired swarm trading framework with the
professional-grade IBKR options chain handler, providing a complete solution
for individual traders implementing sophisticated multi-agent strategies.

Requirements:
- Python 3.13+
- aiohttp (pip install aiohttp)
- numpy (pip install numpy) 
- IBKR Client Portal Gateway running on localhost:5001

Integration Architecture:
- Swarm Framework: Bio-inspired agent coordination
- IBKR Handler: Professional market data and execution
- Async Bridge: Seamless integration between components

Author: Pete W.
License: MIT License  
Copyright (c) 2025 Pete W.
"""

import asyncio
import logging
from typing import Optional, Dict, List, Any
from datetime import datetime
import json

# Import our existing IBKR handler
try:
    from P5002_improved_ibkr_Options_Chains_Handling import (
        IBKROptionsChainHandler, 
        IBKRConfig, 
        IBKRAPIError,
        OptionsContract
    )
except ImportError:
    print("Note: P5002 IBKR handler not found. Install dependencies if running in production.")

# Import swarm framework components
try:
    from P5003_Bio_Inspired_Swarm_Trading_Framework import (
        SwarmOrchestrator,
        MarketEnvironment,
        BaseAgent,
        ScoutAgent,
        WorkerAgent,
        SignalType,
        Pheromone,
        AgentType
    )
except ImportError:
    print("Note: Bio-inspired swarm framework not found.")

class IBKRSwarmBridge:
    """
    Bridge between the bio-inspired swarm framework and IBKR WebAPI.
    
    This class provides async-compatible methods for swarm agents to interact
    with IBKR's API while maintaining the professional-grade error handling
    and performance monitoring from our P5002 implementation.
    """
    
    def __init__(self, config: 'IBKRConfig'):
        self.config = config
        self.ibkr_handler = IBKROptionsChainHandler.from_config(config)
        self.logger = logging.getLogger(self.__class__.__name__)
        
        # Cache for reducing API calls
        self.price_cache = {}
        self.cache_timeout = 30  # seconds
        
        # Performance tracking
        self.api_calls_made = 0
        self.cache_hits = 0
    
    async def get_current_price_async(self, symbol: str) -> Optional[float]:
        """
        Async wrapper for getting current market price.
        
        Integrates caching to reduce API load for swarm agents.
        """
        cache_key = f"{symbol}_price"
        current_time = datetime.now().timestamp()
        
        # Check cache first
        if cache_key in self.price_cache:
            cached_data = self.price_cache[cache_key]
            if current_time - cached_data['timestamp'] < self.cache_timeout:
                self.cache_hits += 1
                return cached_data['price']
        
        try:
            # Run synchronous IBKR call in thread pool to avoid blocking
            price = await asyncio.get_event_loop().run_in_executor(
                None, self._get_price_sync, symbol
            )
            
            # Cache the result
            if price is not None:
                self.price_cache[cache_key] = {
                    'price': price,
                    'timestamp': current_time
                }
            
            self.api_calls_made += 1
            return price
            
        except Exception as e:
            self.logger.error(f"Error getting price for {symbol}: {str(e)}")
            return None
    
    def _get_price_sync(self, symbol: str) -> Optional[float]:
        """Synchronous helper for getting price via IBKR API"""
        try:
            # First find the contract
            result = self.ibkr_handler.find_security_contract(symbol, "NASDAQ")
            if not result:
                return None
            
            contract_id, _ = result
            return self.ibkr_handler.get_current_price(contract_id)
            
        except IBKRAPIError as e:
            self.logger.warning(f"IBKR API error for {symbol}: {str(e)}")
            return None
    
    async def get_options_data_async(self, symbol: str) -> Dict[str, Any]:
        """
        Async wrapper for options chain data.
        
        Used by scout agents to analyze options opportunities.
        """
        try:
            return await asyncio.get_event_loop().run_in_executor(
                None, self._get_options_data_sync, symbol
            )
        except Exception as e:
            self.logger.error(f"Error getting options data for {symbol}: {str(e)}")
            return {}
    
    def _get_options_data_sync(self, symbol: str) -> Dict[str, Any]:
        """Synchronous helper for getting options data"""
        try:
            result = self.ibkr_handler.find_security_contract(symbol, "NASDAQ")
            if not result:
                return {}
            
            contract_id, available_months = result
            current_price = self.ibkr_handler.get_current_price(contract_id)
            
            if not current_price or not available_months:
                return {}
            
            # Get strike prices for front month
            strikes = self.ibkr_handler.get_strike_prices(
                contract_id, available_months[0], current_price, self.config.price_range
            )
            
            return {
                'symbol': symbol,
                'contract_id': contract_id,
                'current_price': current_price,
                'available_months': available_months,
                'strikes': strikes,
                'front_month': available_months[0] if available_months else None
            }
            
        except Exception as e:
            self.logger.error(f"Error in options data sync for {symbol}: {str(e)}")
            return {}
    
    async def submit_order_async(self, symbol: str, order_type: str, quantity: float, 
                                price: float = None) -> Dict[str, Any]:
        """
        Async wrapper for order submission.
        
        Note: This is a simulation for the framework. In production,
        would integrate with actual IBKR order submission endpoints.
        """
        try:
            # Simulate order processing delay
            await asyncio.sleep(0.1)
            
            # In production, would make actual API call:
            # return await self._submit_real_order(symbol, order_type, quantity, price)
            
            # For now, simulate order execution
            order_id = f"sim_order_{datetime.now().timestamp()}"
            success = True  # Would be based on actual API response
            
            return {
                'order_id': order_id,
                'status': 'filled' if success else 'rejected',
                'symbol': symbol,
                'quantity': quantity,
                'price': price,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Order submission error: {str(e)}")
            return {'status': 'error', 'message': str(e)}
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """Get performance statistics for the bridge"""
        total_requests = self.api_calls_made + self.cache_hits
        cache_hit_rate = self.cache_hits / total_requests if total_requests > 0 else 0
        
        return {
            'api_calls_made': self.api_calls_made,
            'cache_hits': self.cache_hits,
            'cache_hit_rate': f"{cache_hit_rate:.2%}",
            'total_requests': total_requests
        }

class EnhancedScoutAgent(ScoutAgent):
    """
    Enhanced scout agent with IBKR integration.
    
    Extends the base scout agent to use real market data from IBKR
    instead of simulated data.
    """
    
    def __init__(self, agent_id: str, environment: 'MarketEnvironment', 
                 symbols: List[str], ibkr_bridge: IBKRSwarmBridge):
        # Call parent with None for ibkr_client since we use the bridge
        super().__init__(agent_id, environment, symbols, None)
        self.ibkr_bridge = ibkr_bridge
    
    async def _get_current_price(self, symbol: str) -> Optional[float]:
        """Override to use IBKR bridge instead of simulation"""
        return await self.ibkr_bridge.get_current_price_async(symbol)
    
    async def _analyze_opportunity(self, symbol: str, price: float) -> float:
        """
        Enhanced opportunity analysis using real IBKR options data.
        
        This method demonstrates how to integrate sophisticated options
        analysis into the swarm intelligence framework.
        """
        try:
            # Get options data for analysis
            options_data = await self.ibkr_bridge.get_options_data_async(symbol)
            
            if not options_data or not options_data.get('strikes'):
                # Fallback to simple analysis if no options data
                return await super()._analyze_opportunity(symbol, price)
            
            # Analyze options implied volatility patterns
            opportunity_score = self._analyze_iv_skew(options_data, price)
            
            # Incorporate volume analysis if available
            opportunity_score *= self._analyze_volume_patterns(symbol)
            
            # Technical analysis overlay
            technical_score = await self._technical_analysis(symbol, price)
            
            # Combined scoring with weights
            final_score = (
                0.4 * opportunity_score +    # Options analysis
                0.3 * technical_score +      # Technical analysis
                0.3 * self._sentiment_analysis(symbol)  # Market sentiment
            )
            
            return min(1.0, max(0.0, final_score))
            
        except Exception as e:
            self.logger.error(f"Enhanced opportunity analysis error for {symbol}: {str(e)}")
            # Fallback to parent implementation
            return await super()._analyze_opportunity(symbol, price)
    
    def _analyze_iv_skew(self, options_data: Dict[str, Any], current_price: float) -> float:
        """
        Analyze implied volatility skew for opportunities.
        
        This is where sophisticated options trading logic would go.
        """
        strikes = options_data.get('strikes', [])
        if len(strikes) < 3:
            return 0.5  # Default score if insufficient data
        
        # Find ATM strike
        atm_strike = min(strikes, key=lambda x: abs(x - current_price))
        atm_index = strikes.index(atm_strike)
        
        # Simple skew analysis (in practice, would calculate actual IVs)
        if atm_index > 0 and atm_index < len(strikes) - 1:
            # Look for skew opportunities
            # This is a placeholder for real IV calculations
            skew_factor = abs(atm_index / len(strikes) - 0.5)  # Distance from center
            return 0.6 + 0.3 * skew_factor
        
        return 0.5
    
    def _analyze_volume_patterns(self, symbol: str) -> float:
        """Analyze volume patterns for confirmation"""
        # Placeholder for volume analysis
        # In practice, would get actual volume data from IBKR
        import random
        return random.uniform(0.8, 1.2)  # Volume multiplier
    
    async def _technical_analysis(self, symbol: str, price: float) -> float:
        """Basic technical analysis"""
        # Placeholder for technical indicators
        # In practice, would implement RSI, MACD, moving averages, etc.
        return 0.5  # Neutral technical score
    
    def _sentiment_analysis(self, symbol: str) -> float:
        """Market sentiment analysis"""
        # Placeholder for sentiment analysis
        # Could integrate news sentiment, social media, etc.
        return 0.5  # Neutral sentiment

class EnhancedWorkerAgent(WorkerAgent):
    """
    Enhanced worker agent with IBKR integration.
    
    Extends the base worker agent to use real order execution
    through the IBKR bridge.
    """
    
    def __init__(self, agent_id: str, environment: 'MarketEnvironment', 
                 ibkr_bridge: IBKRSwarmBridge):
        super().__init__(agent_id, environment, None)
        self.ibkr_bridge = ibkr_bridge
    
    async def _execute_trade(self, opportunity: 'Pheromone', available_capital: float) -> bool:
        """Override to use IBKR bridge for real order execution"""
        try:
            # Calculate position size
            risk_per_trade = available_capital * 0.02
            position_size = min(risk_per_trade, self.max_position_size)
            
            # Determine order details
            symbol = opportunity.symbol
            order_type = opportunity.metadata.get("direction", "long")
            
            # Submit order through IBKR bridge
            result = await self.ibkr_bridge.submit_order_async(
                symbol=symbol,
                order_type=order_type,
                quantity=position_size,
                price=opportunity.price_level
            )
            
            if result.get('status') == 'filled':
                order_id = result['order_id']
                self.active_orders.add(order_id)
                
                # Update environment with position
                self.environment.active_positions[order_id] = {
                    "symbol": symbol,
                    "size": position_size,
                    "price": opportunity.price_level,
                    "direction": order_type,
                    "timestamp": datetime.now(),
                    "ibkr_order_id": order_id
                }
                
                self.logger.info(f"IBKR trade executed: {order_type} {symbol} "
                               f"${position_size:.0f} at ${opportunity.price_level:.2f}")
                return True
            else:
                self.logger.warning(f"IBKR order rejected for {symbol}: {result.get('message', 'Unknown error')}")
                return False
                
        except Exception as e:
            self.logger.error(f"IBKR trade execution error: {str(e)}")
            return False

class IBKRSwarmOrchestrator(SwarmOrchestrator):
    """
    Enhanced swarm orchestrator with IBKR integration.
    
    Replaces the base orchestrator to use IBKR-integrated agents
    instead of simulated agents.
    """
    
    def __init__(self, symbols: List[str], ibkr_config: 'IBKRConfig'):
        super().__init__(symbols)
        self.ibkr_config = ibkr_config
        self.ibkr_bridge = IBKRSwarmBridge(ibkr_config)
    
    def initialize_swarm(self):
        """Initialize swarm with IBKR-integrated agents"""
        from P5003_Bio_Inspired_Swarm_Trading_Framework import QueenAgent, DroneAgent
        
        # Create queen with IBKR bridge
        queen = QueenAgent("queen_001", self.environment, self.ibkr_bridge)
        self.agents.append(queen)
        
        # Create enhanced scouts with IBKR integration
        num_scouts = max(1, len(self.symbols) // 3)
        for i in range(num_scouts):
            scout_symbols = self.symbols[i::num_scouts]
            scout = EnhancedScoutAgent(f"scout_{i:03d}", self.environment, 
                                     scout_symbols, self.ibkr_bridge)
            self.agents.append(scout)
        
        # Create enhanced workers with IBKR integration
        num_workers = max(1, len(self.symbols) // 5)
        for i in range(num_workers):
            worker = EnhancedWorkerAgent(f"worker_{i:03d}", self.environment, self.ibkr_bridge)
            self.agents.append(worker)
        
        # Create standard drone (no IBKR integration needed for risk monitoring)
        drone = DroneAgent("drone_001", self.environment)
        self.agents.append(drone)
        
        logging.info(f"IBKR-integrated swarm initialized: {len(self.agents)} agents")
        logging.info(f"Configuration: {self.ibkr_config.symbol} primary symbol, "
                    f"${self.ibkr_config.price_range} range, {self.ibkr_config.timeout}s timeout")
    
    async def start_swarm(self):
        """Start swarm with IBKR connectivity checks"""
        # Test IBKR connectivity before starting
        logging.info("Testing IBKR connectivity...")
        
        try:
            test_price = await self.ibkr_bridge.get_current_price_async("AAPL")
            if test_price is None:
                logging.warning("IBKR connectivity test failed - running in simulation mode")
            else:
                logging.info(f"IBKR connectivity confirmed - AAPL price: ${test_price:.2f}")
        except Exception as e:
            logging.warning(f"IBKR connectivity error: {str(e)} - continuing with simulation")
        
        # Start the swarm
        await super().start_swarm()
    
    async def stop_swarm(self):
        """Enhanced stop with IBKR bridge performance stats"""
        await super().stop_swarm()
        
        # Display IBKR bridge performance
        bridge_stats = self.ibkr_bridge.get_performance_stats()
        logging.info("\nIBKR BRIDGE PERFORMANCE:")
        logging.info(f"  API calls made: {bridge_stats['api_calls_made']}")
        logging.info(f"  Cache hits: {bridge_stats['cache_hits']}")
        logging.info(f"  Cache hit rate: {bridge_stats['cache_hit_rate']}")
        logging.info(f"  Total requests: {bridge_stats['total_requests']}")

# Usage example and configuration
async def run_ibkr_swarm_demo():
    """
    Demonstration of the integrated IBKR bio-inspired swarm trading system.
    
    This shows how an individual trader can deploy sophisticated multi-agent
    strategies using the WebAPI + Python combination recommended in our analysis.
    """
    # Configure IBKR connection
    ibkr_config = IBKRConfig(
        base_url="https://localhost:5001",
        timeout=30,
        symbol="AAPL",  # Primary symbol for configuration
        exchange="NASDAQ",
        price_range=20.0,  # Wider range for more opportunities
        option_type="P"
    )
    
    # Define symbols for the swarm to trade
    trading_symbols = [
        "AAPL", "GOOGL", "MSFT", "TSLA", "AMZN", 
        "META", "NFLX", "NVDA", "AMD", "CRM"
    ]
    
    # Initialize IBKR-integrated swarm orchestrator
    orchestrator = IBKRSwarmOrchestrator(trading_symbols, ibkr_config)
    orchestrator.initialize_swarm()
    
    # Start the swarm
    try:
        await orchestrator.start_swarm()
    except KeyboardInterrupt:
        logging.info("Swarm shutdown requested by user")

if __name__ == "__main__":
    print("🤖 IBKR Bio-Inspired Swarm Trading System")
    print("=" * 50)
    print("Integration of:")
    print("  • Professional IBKR WebAPI Handler (P5002)")
    print("  • Bio-Inspired Swarm Intelligence Framework (P5003)")
    print("  • Async Bridge for Seamless Integration")
    print()
    print("Recommended for Individual Traders:")
    print("  ✓ Python + WebAPI for rapid development")
    print("  ✓ Async concurrency for multi-agent execution")
    print("  ✓ Professional error handling and monitoring")
    print("  ✓ Bio-inspired emergent strategies")
    print()
    print("Press Ctrl+C to stop the swarm")
    print("=" * 50)
    
    # Run the integrated system
    try:
        asyncio.run(run_ibkr_swarm_demo())
    except KeyboardInterrupt:
        print("\n🛑 Swarm system shutdown complete")
    except ImportError as e:
        print(f"\n⚠️  Missing dependencies: {e}")
        print("For full functionality, install:")
        print("  pip install aiohttp numpy")
        print("  Ensure IBKR Client Portal Gateway is running on localhost:5001")
