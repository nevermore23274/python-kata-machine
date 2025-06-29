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
🥋 Python Kata-Machine - Daily Algorithm Practice

Usage: python kata.py <command> [options]

Daily Practice Commands:
  daily               Generate today's algorithm practice
  test                Run tests for current algorithm
  complete            Mark current algorithm done, advance to next
  progress            Show your progress through the course
  
Utility Commands:
  config              Check configuration
  clear               Clear practice files
  reset               Reset progress and start over
  
Examples:
  python kata.py daily                     # Get today's algorithm
  python kata.py test                      # Test your implementation
  python kata.py complete                  # Mark done, move to next
  python kata.py progress                  # See your progress
  python kata.py clear                     # Clean up files
  python kata.py reset                     # Start course over

Daily Workflow:
  1. python kata.py daily      # Get today's algorithm
  2. cd day1                   # Go to practice directory  
  3. # Edit the algorithm file and implement it
  4. python kata.py test       # Test your implementation
  5. python kata.py complete   # Mark complete, get tomorrow's algorithm
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
        "config": "/kata-machine/check_config.py",
        "daily": "/kata-machine/scripts/daily.py",
        "test": "/kata-machine/test_runner.py",
        "complete": ("/kata-machine/scripts/daily.py", ["complete"]),
        "progress": ("/kata-machine/scripts/daily.py", ["progress"]),
        "clear": "/kata-machine/scripts/clear.py",
        "reset": ("/kata-machine/scripts/daily.py", ["reset"]),
        
        # Legacy commands for backwards compatibility
        "generate": "/kata-machine/scripts/daily.py",  # Redirect to daily
    }
    
    if command in ["help", "-h", "--help"]:
        print_usage()
        return 0
    
    if command not in commands:
        print(f"❌ Unknown command: {command}")
        print_usage()
        return 1
    
    # Handle commands with preset arguments
    if isinstance(commands[command], tuple):
        script_path, preset_args = commands[command]
        final_args = preset_args + remaining_args
    else:
        script_path = commands[command]
        final_args = remaining_args
    
    # Check if script exists
    if not Path(script_path).exists():
        print(f"❌ Script not found: {script_path}")
        return 1
    
    # Run the command
    return run_command(script_path, final_args)


if __name__ == "__main__":
    sys.exit(main())
