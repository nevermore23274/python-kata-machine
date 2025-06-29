#!/usr/bin/env python3
"""
Welcome screen for Python Kata-Machine
Shows ASCII art and quick start commands when entering the container
"""

import os
from pathlib import Path

def show_welcome():
    """Display welcome message with ASCII art and quick commands"""
    
    # ASCII art for Python-Kata
    ascii_art = """
██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗    ██╗  ██╗ █████╗ ████████╗ █████╗ 
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║    ██║ ██╔╝██╔══██╗╚══██╔══╝██╔══██╗
██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║    █████╔╝ ███████║   ██║   ███████║
██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║    ██╔═██╗ ██╔══██║   ██║   ██╔══██║
██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║    ██║  ██╗██║  ██║   ██║   ██║  ██║
╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝
"""
    
    # Color codes
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'
    
    print(f"{BLUE}{ascii_art}{END}")
    print(f"{BOLD}🥋 Welcome to Python Kata-Machine!{END}")
    print(f"{GREEN}Daily algorithm practice following ThePrimeagen's course{END}")
    print()
    
    # Check if user has started
    progress_file = Path(".kata_progress.json")
    if progress_file.exists():
        print(f"{YELLOW}📊 Welcome back! Continue your algorithmic journey...{END}")
    else:
        print(f"{YELLOW}🎯 Ready to start your algorithmic journey!{END}")
    
    print()
    print(f"{BOLD}Quick Start Commands:{END}")
    print(f"  {GREEN}daily{END}               # Get today's algorithm")
    print(f"  {GREEN}test{END}                # Test your implementation")
    print(f"  {GREEN}complete{END}            # Mark done, advance to next")
    print(f"  {GREEN}progress{END}            # See your progress")
    print()
    
    # Show current status
    try:
        import json
        if progress_file.exists():
            with open(progress_file, 'r') as f:
                progress = json.load(f)
            day = progress.get('current_day', 1)
            completed = len(progress.get('completed_algorithms', []))
            print(f"{BOLD}Current Status:{END}")
            print(f"  📅 Day {day}")
            print(f"  ✅ {completed}/25 algorithms completed")
            print(f"  📈 {(completed/25)*100:.1f}% progress")
        else:
            print(f"{BOLD}Getting Started:{END}")
            print(f"  📅 Ready for Day 1")
            print(f"  🎯 25 algorithms to master")
            print(f"  🚀 Run 'python kata.py daily' to begin!")
    except:
        pass
    
    print()
    print(f"{BOLD}Daily Workflow:{END}")
    print(f"  1. {GREEN}daily{END}                # Get algorithm")
    print(f"  2. {GREEN}cd day1{END}              # Go to practice folder")
    print(f"  3. {GREEN}vim algorithm.py{END}     # Implement algorithm")
    print(f"  4. {GREEN}test{END}                 # Test implementation")
    print(f"  5. {GREEN}complete{END}             # Mark done!")
    print()
    print(f"{BLUE}Happy coding! 🎉{END}")
    print(f"Type {GREEN}kata{END} for help or {GREEN}daily{END} to start")
    print()

if __name__ == "__main__":
    show_welcome()
