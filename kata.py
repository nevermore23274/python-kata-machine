#!/usr/bin/env python3
"""
Main entry point for Python Kata-Machine
Provides easy access to all kata-machine functionality
"""

import sys
import subprocess
from pathlib import Path


def print_usage():
    """Print usage information"""
    print("""
🥋 Python Kata-Machine - Main Commands

Usage: python kata.py <command> [options]

Commands:
  config              Check configuration
  generate            Generate new day of practice
  test [options]      Run tests for algorithms
  clear [options]     Clear generated practice days
  setup-tests         Generate test files for all algorithms
  
Examples:
  python kata.py config                    # Check your configuration
  python kata.py generate                  # Create new practice day
  python kata.py test                      # Test latest day
  python kata.py test --day 2              # Test specific day
  python kata.py test --algorithm QuickSort # Test specific algorithm
  python kata.py clear --all               # Clear all practice days
  python kata.py setup-tests               # Generate test templates

Equivalent to original kata-machine:
  yarn generate    →  python kata.py generate
  yarn test        →  python kata.py test
  yarn clear       →  python kata.py clear
    """)


def run_command(script_path: str, args: list = None) -> int:
    """Run a kata-machine script with arguments"""
    cmd = ["python", script_path]
    if args:
        cmd.extend(args)
    
    try:
        result = subprocess.run(cmd)
        return result.returncode
    except FileNotFoundError as e:
        print(f"❌ Error running command: {e}")
        return 1
    except KeyboardInterrupt:
        print("\n⏹️  Command interrupted by user")
        return 130


def main():
    """Main function"""
    if len(sys.argv) < 2:
        print_usage()
        return 1
    
    command = sys.argv[1].lower()
    remaining_args = sys.argv[2:]
    
    # Map commands to scripts
    commands = {
        "config": "check_config.py",
        "generate": "scripts/generate.py", 
        "test": "test_runner.py",
        "clear": "scripts/clear.py",
        "setup-tests": "scripts/generate_tests.py"
    }
    
    if command in ["help", "-h", "--help"]:
        print_usage()
        return 0
    
    if command not in commands:
        print(f"❌ Unknown command: {command}")
        print_usage()
        return 1
    
    script_path = commands[command]
    
    # Check if script exists
    if not Path(script_path).exists():
        print(f"❌ Script not found: {script_path}")
        return 1
    
    # Run the command
    return run_command(script_path, remaining_args)


if __name__ == "__main__":
    sys.exit(main())
