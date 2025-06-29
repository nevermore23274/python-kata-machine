#!/usr/bin/env python3
"""
Configuration checker for Python Kata-Machine
Run this to validate your kata.config.py file
"""

import sys
from pathlib import Path
from config_loader import ConfigLoader


def main():
    """Main function to check configuration"""
    print("🔍 Checking Python Kata-Machine Configuration...\n")
    
    # Check if config file exists
    config_path = Path("kata.config.py")
    if not config_path.exists():
        print("❌ kata.config.py not found!")
        print("   Please create a kata.config.py file in your project root.")
        print("   You can copy the example configuration.")
        return 1
    
    # Try to load and validate configuration
    try:
        loader = ConfigLoader()
        config = loader.load_config()
        
        print("✅ Configuration loaded successfully!")
        print()
        
        # Print summary
        loader.print_config_summary()
        
        # Additional validation
        dsa_list = config["dsa"]
        if len(dsa_list) > 20:
            print("⚠️  Warning: You have more than 20 algorithms selected.")
            print("   This might be overwhelming for daily practice.")
            print("   Consider using one of the preset configurations.")
            print()
        
        if len(dsa_list) < 5:
            print("💡 Tip: You have fewer than 5 algorithms selected.")
            print("   Consider adding more for a well-rounded practice session.")
            print()
        
        print("🎯 Configuration is valid and ready to use!")
        print("   Next step: Run 'python kata.py daily' to start your daily practice.")
        
        return 0
        
    except Exception as e:
        print(f"❌ Configuration Error: {e}")
        print()
        print("🔧 Please fix the error in your kata.config.py file and try again.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
