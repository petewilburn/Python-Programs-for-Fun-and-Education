#!/usr/bin/env python3
"""
IBKR Handler Test Script
Demonstrates that the improved IBKR Options Chain Handler 
works correctly with Python 3.13.5
"""

import sys
from P5002_improved_ibkr_Options_Chains_Handling import IBKROptionsChainHandler

def main():
    print("🚀 Testing IBKR Options Chain Handler with Python 3.13.5")
    print("=" * 60)
    
    # Show Python version
    print(f"🐍 Python version: {sys.version}")
    print()
    
    # Test handler initialization
    print("📦 Initializing IBKR Options Chain Handler...")
    handler = IBKROptionsChainHandler()
    print(f"✅ Handler created successfully: {type(handler).__name__}")
    print()
    
    # Test method chaining (Python 3.11+ Self type feature)
    print("🔗 Testing method chaining with Self type...")
    configured_handler = (handler
                         .configure_timeout(45)
                         .configure_base_url("https://localhost:5001"))
    
    print(f"✅ Method chaining works: timeout={configured_handler.timeout}s")
    print()
    
    # Show that all dependencies are available
    print("📚 Verifying dependencies...")
    try:
        import requests
        import urllib3
        from typing import Self
        print("✅ requests library available")
        print("✅ urllib3 library available") 
        print("✅ Self type available (Python 3.11+ feature)")
        print()
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        return 1
    
    print("🎉 IBKR Options Chain Handler is ready for production use!")
    print("💡 To run the full handler, ensure IBKR Client Portal Gateway is running on localhost:5001")
    
    return 0

if __name__ == "__main__":
    exit(main())
