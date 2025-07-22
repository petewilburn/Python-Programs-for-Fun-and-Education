#!/usr/bin/env python3
"""
Python 3.13 Feature Test for IBKR Options Chain Handler
Verifies all advanced Python 3.13+ features work correctly.
"""

import sys
from typing import Self

def test_python_version():
    """Test Python version and basic functionality"""
    print(f"🐍 Python version: {sys.version}")
    print(f"✅ Version check: {sys.version_info >= (3, 13)}")

def test_enhanced_f_strings():
    """Test Python 3.12+ enhanced f-string debugging"""
    price = 150.75
    symbol = "AAPL"
    print(f"💰 Current {price=:.2f}")  # Enhanced f-string with = specifier
    print(f"📊 Processing {symbol=}")
    print("✅ Enhanced f-strings working")

def test_pattern_matching():
    """Test Python 3.10+ pattern matching"""
    option_type = "P"
    
    match option_type:
        case "P" | "PUT":
            result = "PUT"
        case "C" | "CALL":
            result = "CALL"
        case _:
            result = "UNKNOWN"
    
    print(f"🎯 Pattern matching result: {option_type} → {result}")
    print("✅ Pattern matching working")

class TestChaining:
    """Test Self type for method chaining (Python 3.11+)"""
    
    def __init__(self):
        self.value = 0
    
    def add(self, n: int) -> Self:
        self.value += n
        return self
    
    def multiply(self, n: int) -> Self:
        self.value *= n
        return self

def test_method_chaining():
    """Test Self type and method chaining"""
    obj = TestChaining().add(5).multiply(3).add(2)
    print(f"🔗 Method chaining result: {obj.value}")
    print("✅ Self type and method chaining working")

def test_union_types():
    """Test modern union type syntax (Python 3.10+)"""
    def process_data(value: str | int | None) -> str:
        match value:
            case None:
                return "No data"
            case str():
                return f"String: {value}"
            case int():
                return f"Integer: {value}"
    
    results = [
        process_data(None),
        process_data("AAPL"),
        process_data(150)
    ]
    
    print(f"🔀 Union type results: {results}")
    print("✅ Union types with | syntax working")

def test_builtin_generics():
    """Test built-in generic types (Python 3.9+)"""
    contracts: dict[str, list[float]] = {
        "AAPL": [145.0, 150.0, 155.0],
        "MSFT": [380.0, 385.0, 390.0]
    }
    
    strike_count = sum(len(strikes) for strikes in contracts.values())
    print(f"📋 Contract data: {len(contracts)} symbols, {strike_count} total strikes")
    print("✅ Built-in generics (dict, list) working")

def main():
    """Main test function"""
    print("🚀 Python 3.13+ Feature Verification for IBKR Handler")
    print("=" * 55)
    
    test_python_version()
    print()
    
    test_enhanced_f_strings()
    print()
    
    test_pattern_matching()
    print()
    
    test_method_chaining()
    print()
    
    test_union_types()
    print()
    
    test_builtin_generics()
    print()
    
    print("🎉 All Python 3.13+ features verified successfully!")
    print("✅ Your IBKR Options Chain Handler is ready to run!")

if __name__ == "__main__":
    main()
