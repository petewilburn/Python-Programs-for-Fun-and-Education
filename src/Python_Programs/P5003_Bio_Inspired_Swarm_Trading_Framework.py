#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bio-Inspired Agentic Swarm Trading Framework

A hierarchical multi-agent trading system inspired by biological swarm intelligence,
specifically ant colony optimization and bee colony algorithms. This framework
demonstrates how individual agents can coordinate through stigmergy and emergent
behavior to execute sophisticated trading strategies.

Architecture:
- Queen Agent: Strategic oversight and resource allocation
- Scout Agents: Market opportunity discovery
- Worker Agents: Order execution and position management
- Drone Agents: Risk monitoring and compliance
- Environment: Shared market state and pheromone trails

Requirements:
- Python 3.13+
- asyncio for concurrent agent execution
- IBKR Client Portal Gateway running on localhost:5001
- Real-time market data subscriptions

Bio-Inspired Concepts:
- Stigmergy: Indirect coordination through environment modification
- Pheromone Trails: Signal strength indicating opportunity quality
- Emergent Behavior: Complex strategies from simple agent interactions
- Adaptive Roles: Dynamic agent specialization based on market conditions

Author: Pete W.
License: MIT License
Copyright (c) 2025 Pete W.
"""

import asyncio
import aiohttp
import logging
import json
import numpy as np
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set, Callable, Any
from enum import Enum, auto
import weakref
from collections import defaultdict, deque
import random
import math

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

class AgentType(Enum):
    """Types of agents in the swarm hierarchy"""
    QUEEN = auto()      # Strategic oversight
    SCOUT = auto()      # Opportunity discovery
    WORKER = auto()     # Trade execution
    DRONE = auto()      # Risk monitoring

class SignalType(Enum):
    """Types of signals agents can emit"""
    OPPORTUNITY = auto()    # Market opportunity detected
    DANGER = auto()         # Risk alert
    RESOURCES = auto()      # Capital allocation
    COORDINATION = auto()   # Inter-agent coordination

@dataclass
class Pheromone:
    """
    Pheromone trail representing market signals and agent communication.
    
    Inspired by ant colony optimization where pheromones guide collective behavior.
    """
    signal_type: SignalType
    strength: float
    symbol: str
    price_level: float
    timestamp: datetime
    source_agent_id: str
    decay_rate: float = 0.05  # How quickly pheromone evaporates
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def age_minutes(self) -> float:
        """Calculate age of pheromone in minutes"""
        return (datetime.now() - self.timestamp).total_seconds() / 60
    
    def current_strength(self) -> float:
        """Calculate current pheromone strength accounting for decay"""
        age = self.age_minutes()
        return self.strength * math.exp(-self.decay_rate * age)
    
    def is_expired(self, max_age_minutes: float = 30) -> bool:
        """Check if pheromone has expired"""
        return self.age_minutes() > max_age_minutes or self.current_strength() < 0.01

@dataclass
class MarketEnvironment:
    """
    Shared environment where agents operate and communicate through stigmergy.
    
    This represents the "nest" or "hive" where information is deposited and
    retrieved by agents, enabling indirect coordination.
    """
    pheromone_trails: List[Pheromone] = field(default_factory=list)
    market_data: Dict[str, Dict] = field(default_factory=dict)
    active_positions: Dict[str, Dict] = field(default_factory=dict)
    resource_allocation: Dict[str, float] = field(default_factory=dict)
    risk_metrics: Dict[str, float] = field(default_factory=dict)
    
    def add_pheromone(self, pheromone: Pheromone):
        """Add pheromone trail to environment"""
        self.pheromone_trails.append(pheromone)
        self._cleanup_expired_pheromones()
    
    def _cleanup_expired_pheromones(self):
        """Remove expired pheromones to maintain environment cleanliness"""
        self.pheromone_trails = [p for p in self.pheromone_trails if not p.is_expired()]
    
    def get_pheromones_by_type(self, signal_type: SignalType, symbol: str = None) -> List[Pheromone]:
        """Retrieve pheromones of specific type, optionally filtered by symbol"""
        pheromones = [p for p in self.pheromone_trails 
                     if p.signal_type == signal_type and not p.is_expired()]
        
        if symbol:
            pheromones = [p for p in pheromones if p.symbol == symbol]
        
        # Sort by current strength (strongest first)
        return sorted(pheromones, key=lambda p: p.current_strength(), reverse=True)
    
    def get_signal_strength(self, signal_type: SignalType, symbol: str, price_level: float) -> float:
        """
        Calculate aggregated signal strength around a price level.
        
        This mimics how biological agents sense pheromone concentration gradients.
        """
        relevant_pheromones = self.get_pheromones_by_type(signal_type, symbol)
        
        total_strength = 0.0
        for pheromone in relevant_pheromones:
            # Distance-based weighting (closer pheromones have more influence)
            price_distance = abs(pheromone.price_level - price_level)
            distance_weight = math.exp(-price_distance / 5.0)  # 5% price tolerance
            
            total_strength += pheromone.current_strength() * distance_weight
        
        return total_strength

class BaseAgent(ABC):
    """
    Base class for all swarm agents.
    
    Implements common behaviors like pheromone sensing, communication,
    and basic lifecycle management.
    """
    
    def __init__(self, agent_id: str, agent_type: AgentType, environment: MarketEnvironment):
        self.agent_id = agent_id
        self.agent_type = agent_type
        self.environment = environment
        self.logger = logging.getLogger(f"{agent_type.name}_{agent_id}")
        self.active = True
        self.last_action_time = datetime.now()
        self.energy_level = 1.0  # Biological metaphor for agent capacity
        self.specialization_score = defaultdict(float)  # Adaptive specialization
        
        # Performance tracking
        self.actions_taken = 0
        self.successful_actions = 0
        self.total_pnl_contribution = 0.0
    
    @abstractmethod
    async def execute_cycle(self):
        """Main execution cycle for the agent - must be implemented by subclasses"""
        pass
    
    def emit_pheromone(self, signal_type: SignalType, symbol: str, price_level: float, 
                      strength: float, metadata: Dict[str, Any] = None):
        """Emit pheromone trail for other agents to detect"""
        pheromone = Pheromone(
            signal_type=signal_type,
            strength=strength,
            symbol=symbol,
            price_level=price_level,
            timestamp=datetime.now(),
            source_agent_id=self.agent_id,
            metadata=metadata or {}
        )
        
        self.environment.add_pheromone(pheromone)
        self.logger.debug(f"Emitted {signal_type.name} pheromone for {symbol} at ${price_level:.2f}")
    
    def sense_environment(self, signal_type: SignalType, symbol: str = None) -> List[Pheromone]:
        """Sense pheromone trails in the environment"""
        return self.environment.get_pheromones_by_type(signal_type, symbol)
    
    def update_energy(self, delta: float):
        """Update agent energy level (biological fatigue simulation)"""
        self.energy_level = max(0.0, min(1.0, self.energy_level + delta))
        
        if self.energy_level < 0.1:
            self.logger.warning(f"Agent {self.agent_id} energy critically low: {self.energy_level:.2f}")
    
    def should_rest(self) -> bool:
        """Determine if agent should rest based on energy and market conditions"""
        return self.energy_level < 0.3 or not self.active

class QueenAgent(BaseAgent):
    """
    Queen Agent: Strategic oversight and resource allocation.
    
    Like a queen bee, this agent doesn't directly execute trades but coordinates
    the overall swarm strategy and allocates resources to different sub-swarms.
    """
    
    def __init__(self, agent_id: str, environment: MarketEnvironment, ibkr_client):
        super().__init__(agent_id, AgentType.QUEEN, environment)
        self.ibkr_client = ibkr_client
        self.managed_symbols = set()
        self.resource_budget = 100000.0  # Total capital to manage
        self.risk_tolerance = 0.02  # 2% portfolio risk limit
        
    async def execute_cycle(self):
        """Queen's main cycle: resource allocation and strategic oversight"""
        try:
            await self._assess_swarm_performance()
            await self._allocate_resources()
            await self._coordinate_swarm_strategy()
            await self._monitor_risk()
            
            self.update_energy(-0.01)  # Queens work constantly but slowly deplete
            
        except Exception as e:
            self.logger.error(f"Queen cycle error: {str(e)}")
    
    async def _assess_swarm_performance(self):
        """Evaluate performance of different agent types and strategies"""
        # Analyze pheromone patterns to understand swarm behavior
        opportunity_signals = self.sense_environment(SignalType.OPPORTUNITY)
        danger_signals = self.sense_environment(SignalType.DANGER)
        
        # Calculate swarm health metrics
        opportunity_density = len(opportunity_signals)
        risk_density = len(danger_signals)
        
        if risk_density > opportunity_density * 2:
            # High risk environment - reduce overall activity
            self.emit_pheromone(SignalType.COORDINATION, "SYSTEM", 0.0, 0.8,
                              {"action": "reduce_activity", "reason": "high_risk_environment"})
            self.logger.warning("High risk environment detected - signaling activity reduction")
    
    async def _allocate_resources(self):
        """Allocate capital resources based on opportunity strength"""
        symbol_opportunities = defaultdict(float)
        
        # Aggregate opportunity signals by symbol
        opportunities = self.sense_environment(SignalType.OPPORTUNITY)
        for opp in opportunities:
            symbol_opportunities[opp.symbol] += opp.current_strength()
        
        # Proportional resource allocation
        total_opportunity = sum(symbol_opportunities.values())
        if total_opportunity > 0:
            for symbol, strength in symbol_opportunities.items():
                allocation_ratio = strength / total_opportunity
                allocated_capital = self.resource_budget * allocation_ratio * 0.1  # Conservative 10% max
                
                self.environment.resource_allocation[symbol] = allocated_capital
                
                # Emit resource availability signal
                self.emit_pheromone(SignalType.RESOURCES, symbol, 0.0, allocation_ratio,
                                  {"allocated_capital": allocated_capital})
    
    async def _coordinate_swarm_strategy(self):
        """Coordinate overall swarm strategy based on market conditions"""
        # Simple market regime detection
        market_volatility = await self._estimate_market_volatility()
        
        if market_volatility > 0.25:  # High volatility
            strategy_signal = {"regime": "high_volatility", "recommended_action": "defensive"}
        elif market_volatility < 0.10:  # Low volatility
            strategy_signal = {"regime": "low_volatility", "recommended_action": "opportunistic"}
        else:
            strategy_signal = {"regime": "normal", "recommended_action": "balanced"}
        
        self.emit_pheromone(SignalType.COORDINATION, "MARKET", market_volatility, 0.7, strategy_signal)
    
    async def _estimate_market_volatility(self) -> float:
        """Simple volatility estimation based on recent market activity"""
        # In a real implementation, this would use actual market data
        return random.uniform(0.08, 0.30)  # Placeholder
    
    async def _monitor_risk(self):
        """Monitor overall portfolio risk and emit warnings if necessary"""
        total_exposure = sum(abs(pos.get('value', 0)) for pos in self.environment.active_positions.values())
        risk_ratio = total_exposure / self.resource_budget
        
        if risk_ratio > self.risk_tolerance:
            self.emit_pheromone(SignalType.DANGER, "PORTFOLIO", risk_ratio, 0.9,
                              {"risk_type": "portfolio_overexposure", "current_ratio": risk_ratio})
            self.logger.warning(f"Portfolio risk exceeded: {risk_ratio:.2%}")

class ScoutAgent(BaseAgent):
    """
    Scout Agent: Market opportunity discovery.
    
    Like scout bees, these agents explore the market landscape looking for
    profitable opportunities and report back to the swarm.
    """
    
    def __init__(self, agent_id: str, environment: MarketEnvironment, symbols: List[str], ibkr_client):
        super().__init__(agent_id, AgentType.SCOUT, environment)
        self.assigned_symbols = symbols
        self.ibkr_client = ibkr_client
        self.discovery_radius = 0.05  # 5% price range to explore
        
    async def execute_cycle(self):
        """Scout's main cycle: explore market and identify opportunities"""
        if self.should_rest():
            await asyncio.sleep(1)
            return
        
        try:
            for symbol in self.assigned_symbols:
                await self._scout_symbol(symbol)
            
            self.update_energy(-0.02)  # Scouting is energy intensive
            await asyncio.sleep(0.1)  # Brief rest between cycles
            
        except Exception as e:
            self.logger.error(f"Scout cycle error: {str(e)}")
    
    async def _scout_symbol(self, symbol: str):
        """Scout a specific symbol for trading opportunities"""
        try:
            # Get current market data (using our P5002 handler as base)
            current_price = await self._get_current_price(symbol)
            if not current_price:
                return
            
            # Look for technical patterns or anomalies
            opportunity_score = await self._analyze_opportunity(symbol, current_price)
            
            if opportunity_score > 0.6:  # High-quality opportunity
                self.emit_pheromone(
                    SignalType.OPPORTUNITY, symbol, current_price, opportunity_score,
                    {
                        "analysis_type": "technical_pattern",
                        "confidence": opportunity_score,
                        "scout_id": self.agent_id
                    }
                )
                self.logger.info(f"Opportunity detected: {symbol} at ${current_price:.2f} (score: {opportunity_score:.2f})")
                self.successful_actions += 1
                
            self.actions_taken += 1
            
        except Exception as e:
            self.logger.error(f"Error scouting {symbol}: {str(e)}")
    
    async def _get_current_price(self, symbol: str) -> Optional[float]:
        """Get current market price for symbol"""
        # Integration with our P5002 IBKR handler
        # In real implementation, would use actual API call
        return random.uniform(100, 200)  # Placeholder
    
    async def _analyze_opportunity(self, symbol: str, price: float) -> float:
        """
        Analyze market opportunity using technical indicators.
        
        Returns opportunity score between 0 and 1.
        """
        # Placeholder for sophisticated technical analysis
        # In practice, would implement:
        # - Moving average crossovers
        # - RSI divergences
        # - Volume anomalies
        # - Options flow analysis
        
        # Simple random walk analysis (placeholder)
        volatility = random.uniform(0.1, 0.3)
        momentum = random.uniform(-0.1, 0.1)
        volume_spike = random.choice([True, False])
        
        base_score = 0.5
        if momentum > 0.05:
            base_score += 0.2
        if volatility > 0.25:
            base_score += 0.1
        if volume_spike:
            base_score += 0.15
        
        return min(1.0, base_score)

class WorkerAgent(BaseAgent):
    """
    Worker Agent: Trade execution and position management.
    
    Like worker bees, these agents execute the actual trading based on
    opportunities discovered by scouts and resources allocated by the queen.
    """
    
    def __init__(self, agent_id: str, environment: MarketEnvironment, ibkr_client):
        super().__init__(agent_id, AgentType.WORKER, environment)
        self.ibkr_client = ibkr_client
        self.max_position_size = 10000.0  # Maximum position size
        self.active_orders = set()
        
    async def execute_cycle(self):
        """Worker's main cycle: execute trades based on swarm intelligence"""
        if self.should_rest():
            await asyncio.sleep(2)
            self.update_energy(0.05)  # Workers recover energy during rest
            return
        
        try:
            await self._process_opportunities()
            await self._manage_positions()
            self.update_energy(-0.03)  # Trading is energy intensive
            
        except Exception as e:
            self.logger.error(f"Worker cycle error: {str(e)}")
    
    async def _process_opportunities(self):
        """Process opportunity signals and execute trades"""
        opportunities = self.sense_environment(SignalType.OPPORTUNITY)
        
        for opportunity in opportunities[:3]:  # Process top 3 opportunities
            # Check if resources are available
            available_capital = self.environment.resource_allocation.get(opportunity.symbol, 0)
            
            if available_capital < 1000:  # Minimum trade size
                continue
            
            # Check for competing signals
            dangers = self.sense_environment(SignalType.DANGER, opportunity.symbol)
            if any(d.current_strength() > opportunity.current_strength() for d in dangers):
                self.logger.info(f"Skipping {opportunity.symbol} due to risk signals")
                continue
            
            # Execute trade
            success = await self._execute_trade(opportunity, available_capital)
            if success:
                self.successful_actions += 1
                # Reinforce successful pheromone trail
                self.emit_pheromone(
                    SignalType.OPPORTUNITY, opportunity.symbol, opportunity.price_level,
                    opportunity.current_strength() * 0.8,  # Reinforce but don't amplify
                    {"reinforcement": True, "worker_id": self.agent_id}
                )
            
            self.actions_taken += 1
    
    async def _execute_trade(self, opportunity: Pheromone, available_capital: float) -> bool:
        """Execute actual trade based on opportunity signal"""
        try:
            # Calculate position size based on opportunity strength and available capital
            risk_per_trade = available_capital * 0.02  # 2% risk per trade
            position_size = min(risk_per_trade, self.max_position_size)
            
            # Determine trade direction based on opportunity metadata
            trade_direction = opportunity.metadata.get("direction", "long")
            
            # Simulate order execution
            order_id = f"order_{self.agent_id}_{len(self.active_orders)}"
            
            # In real implementation, would use actual IBKR API
            # success = await self.ibkr_client.submit_order(...)
            
            # Simulate execution
            execution_success = random.choice([True, True, True, False])  # 75% success rate
            
            if execution_success:
                self.active_orders.add(order_id)
                self.environment.active_positions[order_id] = {
                    "symbol": opportunity.symbol,
                    "size": position_size,
                    "price": opportunity.price_level,
                    "direction": trade_direction,
                    "timestamp": datetime.now()
                }
                
                self.logger.info(f"Trade executed: {trade_direction} {opportunity.symbol} "
                               f"${position_size:.0f} at ${opportunity.price_level:.2f}")
                return True
            else:
                self.logger.warning(f"Trade execution failed for {opportunity.symbol}")
                return False
                
        except Exception as e:
            self.logger.error(f"Trade execution error: {str(e)}")
            return False
    
    async def _manage_positions(self):
        """Manage existing positions based on market conditions"""
        # Check for exit signals on active positions
        for order_id in list(self.active_orders):
            position = self.environment.active_positions.get(order_id)
            if not position:
                continue
            
            symbol = position["symbol"]
            entry_price = position["price"]
            
            # Check for danger signals
            dangers = self.sense_environment(SignalType.DANGER, symbol)
            high_risk = any(d.current_strength() > 0.7 for d in dangers)
            
            # Simple exit logic
            position_age = (datetime.now() - position["timestamp"]).total_seconds() / 3600
            should_exit = high_risk or position_age > 24  # Exit if high risk or position older than 24h
            
            if should_exit:
                success = await self._close_position(order_id, position)
                if success:
                    self.active_orders.discard(order_id)
    
    async def _close_position(self, order_id: str, position: Dict) -> bool:
        """Close an existing position"""
        try:
            # Simulate position closing
            # In real implementation: await self.ibkr_client.close_position(...)
            
            pnl = random.uniform(-500, 1000)  # Simulated P&L
            self.total_pnl_contribution += pnl
            
            del self.environment.active_positions[order_id]
            
            self.logger.info(f"Position closed: {position['symbol']} P&L: ${pnl:.2f}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error closing position {order_id}: {str(e)}")
            return False

class DroneAgent(BaseAgent):
    """
    Drone Agent: Risk monitoring and compliance.
    
    Like drone bees that patrol the hive, these agents monitor for risks
    and ensure the swarm operates within defined parameters.
    """
    
    def __init__(self, agent_id: str, environment: MarketEnvironment):
        super().__init__(agent_id, AgentType.DRONE, environment)
        self.risk_thresholds = {
            "max_drawdown": 0.05,  # 5% maximum drawdown
            "max_correlation": 0.8,  # Maximum position correlation
            "max_exposure": 0.3     # Maximum single-asset exposure
        }
    
    async def execute_cycle(self):
        """Drone's main cycle: monitor risks and emit warnings"""
        try:
            await self._monitor_portfolio_risk()
            await self._monitor_concentration_risk()
            await self._monitor_correlation_risk()
            
            self.update_energy(-0.01)  # Monitoring is less energy intensive
            await asyncio.sleep(5)  # Longer cycle for risk monitoring
            
        except Exception as e:
            self.logger.error(f"Drone cycle error: {str(e)}")
    
    async def _monitor_portfolio_risk(self):
        """Monitor overall portfolio risk metrics"""
        total_value = sum(abs(pos.get('size', 0)) for pos in self.environment.active_positions.values())
        
        if total_value > 0:
            # Calculate simple risk metrics
            positions_by_symbol = defaultdict(float)
            for pos in self.environment.active_positions.values():
                positions_by_symbol[pos['symbol']] += abs(pos.get('size', 0))
            
            # Check for concentration risk
            max_position = max(positions_by_symbol.values()) if positions_by_symbol else 0
            concentration_ratio = max_position / total_value if total_value > 0 else 0
            
            if concentration_ratio > self.risk_thresholds["max_exposure"]:
                self.emit_pheromone(
                    SignalType.DANGER, "PORTFOLIO", concentration_ratio, 0.8,
                    {
                        "risk_type": "concentration",
                        "max_symbol": max(positions_by_symbol.keys(), key=positions_by_symbol.get),
                        "concentration_ratio": concentration_ratio
                    }
                )
                self.logger.warning(f"Concentration risk detected: {concentration_ratio:.2%}")
    
    async def _monitor_concentration_risk(self):
        """Monitor for excessive concentration in single assets"""
        symbol_exposures = defaultdict(float)
        
        for position in self.environment.active_positions.values():
            symbol = position['symbol']
            exposure = abs(position.get('size', 0))
            symbol_exposures[symbol] += exposure
        
        total_exposure = sum(symbol_exposures.values())
        
        if total_exposure > 0:
            for symbol, exposure in symbol_exposures.items():
                concentration = exposure / total_exposure
                if concentration > self.risk_thresholds["max_exposure"]:
                    self.emit_pheromone(
                        SignalType.DANGER, symbol, 0.0, concentration,
                        {"risk_type": "single_asset_concentration", "exposure_ratio": concentration}
                    )
    
    async def _monitor_correlation_risk(self):
        """Monitor for excessive correlation between positions"""
        # Simplified correlation check
        symbols = list(set(pos['symbol'] for pos in self.environment.active_positions.values()))
        
        if len(symbols) > 1:
            # In a real implementation, would calculate actual correlations
            # For now, emit warning if too many similar sector positions
            if len(symbols) > 5:  # Rough diversification check
                correlation_risk = 0.3  # Low risk with many symbols
            else:
                correlation_risk = 0.8  # High risk with few symbols
            
            if correlation_risk > self.risk_thresholds["max_correlation"]:
                self.emit_pheromone(
                    SignalType.DANGER, "CORRELATION", 0.0, correlation_risk,
                    {"risk_type": "portfolio_correlation", "num_symbols": len(symbols)}
                )

class SwarmOrchestrator:
    """
    Central orchestrator for the bio-inspired trading swarm.
    
    Manages the lifecycle of all agents and coordinates their execution.
    """
    
    def __init__(self, symbols: List[str]):
        self.environment = MarketEnvironment()
        self.agents: List[BaseAgent] = []
        self.symbols = symbols
        self.ibkr_client = None  # Would initialize actual IBKR client here
        self.running = False
        
    def initialize_swarm(self):
        """Initialize the swarm with appropriate agent composition"""
        # Create one queen for strategic oversight
        queen = QueenAgent("queen_001", self.environment, self.ibkr_client)
        self.agents.append(queen)
        
        # Create scouts for opportunity discovery (1 per 3 symbols)
        num_scouts = max(1, len(self.symbols) // 3)
        for i in range(num_scouts):
            scout_symbols = self.symbols[i::num_scouts]  # Distribute symbols among scouts
            scout = ScoutAgent(f"scout_{i:03d}", self.environment, scout_symbols, self.ibkr_client)
            self.agents.append(scout)
        
        # Create workers for trade execution (1 per 5 symbols)
        num_workers = max(1, len(self.symbols) // 5)
        for i in range(num_workers):
            worker = WorkerAgent(f"worker_{i:03d}", self.environment, self.ibkr_client)
            self.agents.append(worker)
        
        # Create drones for risk monitoring (1 per swarm)
        drone = DroneAgent("drone_001", self.environment)
        self.agents.append(drone)
        
        logging.info(f"Swarm initialized: {len(self.agents)} agents "
                    f"({num_scouts} scouts, {num_workers} workers, 1 queen, 1 drone)")
    
    async def start_swarm(self):
        """Start the swarm execution"""
        self.running = True
        logging.info("Starting bio-inspired trading swarm...")
        
        # Create tasks for all agents
        agent_tasks = []
        for agent in self.agents:
            task = asyncio.create_task(self._run_agent(agent))
            agent_tasks.append(task)
        
        # Create monitoring task
        monitor_task = asyncio.create_task(self._monitor_swarm())
        
        try:
            # Run all agents concurrently
            await asyncio.gather(*agent_tasks, monitor_task)
        except KeyboardInterrupt:
            logging.info("Swarm execution interrupted by user")
        finally:
            await self.stop_swarm()
    
    async def _run_agent(self, agent: BaseAgent):
        """Run individual agent in continuous loop"""
        while self.running and agent.active:
            try:
                await agent.execute_cycle()
                
                # Dynamic rest periods based on agent type
                if agent.agent_type == AgentType.SCOUT:
                    await asyncio.sleep(0.5)  # Scouts work frequently
                elif agent.agent_type == AgentType.WORKER:
                    await asyncio.sleep(1.0)  # Workers moderate frequency
                elif agent.agent_type == AgentType.QUEEN:
                    await asyncio.sleep(10.0)  # Queen works infrequently
                else:  # Drone
                    await asyncio.sleep(5.0)  # Drones moderate frequency
                    
            except Exception as e:
                logging.error(f"Error in agent {agent.agent_id}: {str(e)}")
                await asyncio.sleep(5)  # Error recovery delay
    
    async def _monitor_swarm(self):
        """Monitor overall swarm health and performance"""
        while self.running:
            try:
                # Calculate swarm metrics
                total_agents = len(self.agents)
                active_agents = sum(1 for agent in self.agents if agent.active)
                total_actions = sum(agent.actions_taken for agent in self.agents)
                successful_actions = sum(agent.successful_actions for agent in self.agents)
                
                success_rate = successful_actions / total_actions if total_actions > 0 else 0
                
                # Log swarm status
                logging.info(f"Swarm Status: {active_agents}/{total_agents} agents active, "
                           f"{total_actions} actions taken, {success_rate:.2%} success rate")
                
                # Check pheromone trail health
                active_pheromones = len(self.environment.pheromone_trails)
                logging.info(f"Environment: {active_pheromones} active pheromone trails")
                
                await asyncio.sleep(30)  # Monitor every 30 seconds
                
            except Exception as e:
                logging.error(f"Swarm monitoring error: {str(e)}")
                await asyncio.sleep(10)
    
    async def stop_swarm(self):
        """Gracefully stop the swarm"""
        logging.info("Stopping swarm...")
        self.running = False
        
        # Deactivate all agents
        for agent in self.agents:
            agent.active = False
        
        # Final performance report
        self._generate_performance_report()
    
    def _generate_performance_report(self):
        """Generate final performance report"""
        logging.info("=" * 50)
        logging.info("SWARM PERFORMANCE REPORT")
        logging.info("=" * 50)
        
        for agent in self.agents:
            success_rate = (agent.successful_actions / agent.actions_taken 
                          if agent.actions_taken > 0 else 0)
            
            logging.info(f"{agent.agent_type.name} {agent.agent_id}:")
            logging.info(f"  Actions: {agent.actions_taken}")
            logging.info(f"  Success Rate: {success_rate:.2%}")
            logging.info(f"  Energy Level: {agent.energy_level:.2f}")
            
            if hasattr(agent, 'total_pnl_contribution'):
                logging.info(f"  P&L Contribution: ${agent.total_pnl_contribution:.2f}")
        
        total_pnl = sum(getattr(agent, 'total_pnl_contribution', 0) for agent in self.agents)
        logging.info(f"\nTotal Swarm P&L: ${total_pnl:.2f}")
        logging.info("=" * 50)

# Example usage and demonstration
async def main():
    """
    Demonstration of the bio-inspired swarm trading system
    """
    # Define symbols to trade
    symbols = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN", "META", "NFLX"]
    
    # Initialize swarm orchestrator
    orchestrator = SwarmOrchestrator(symbols)
    orchestrator.initialize_swarm()
    
    # Start swarm execution
    try:
        await orchestrator.start_swarm()
    except KeyboardInterrupt:
        print("\nShutting down swarm...")

if __name__ == "__main__":
    print("🐝 Bio-Inspired Agentic Swarm Trading Framework")
    print("=" * 50)
    print("Press Ctrl+C to stop the swarm")
    print()
    
    # Run the swarm
    asyncio.run(main())
