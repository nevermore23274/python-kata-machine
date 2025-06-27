#!/usr/bin/env python3
"""
Clear generated practice folders for Python Kata-Machine
Equivalent to 'yarn clear' in the original kata-machine
"""

import os
import sys
import shutil
from pathlib import Path
from typing import List


class KataClearer:
    """Clears generated practice folders"""
    
    def __init__(self, base_dir: Path = None):
        self.base_dir = base_dir or Path.cwd()
        self.src_dir = self.base_dir / "src"
    
    def find_day_directories(self) -> List[Path]:
        """Find all day directories that can be cleared"""
        day_dirs = []
        
        if not self.src_dir.exists():
            return day_dirs
        
        for item in self.src_dir.iterdir():
            if item.is_dir() and item.name.startswith("day"):
                try:
                    # Validate it's a day directory (dayN format)
                    int(item.name[3:])  # This will raise ValueError if not a number
                    day_dirs.append(item)
                except ValueError:
                    continue
        
        # Sort by day number
        day_dirs.sort(key=lambda x: int(x.name[3:]))
        return day_dirs
    
    def clear_all_days(self, confirm: bool = True) -> int:
        """Clear all generated day directories"""
        day_dirs = self.find_day_directories()
        
        if not day_dirs:
            print("📭 No practice days found to clear.")
            print("   The src/ directory is already clean.")
            return 0
        
        print(f"🗑️  Found {len(day_dirs)} practice day(s) to clear:")
        for day_dir in day_dirs:
            print(f"   📁 {day_dir}")
        print()
        
        if confirm:
            response = input("❓ Are you sure you want to delete all practice days? (y/N): ")
            if response.lower() not in ['y', 'yes']:
                print("❌ Clear operation cancelled.")
                return 1
        
        print("🧹 Clearing practice days...")
        cleared_count = 0
        
        for day_dir in day_dirs:
            try:
                shutil.rmtree(day_dir)
                print(f"   ✅ Removed {day_dir.name}")
                cleared_count += 1
            except Exception as e:
                print(f"   ❌ Error removing {day_dir.name}: {e}")
        
        # Remove src directory if it's empty
        try:
            if self.src_dir.exists() and not any(self.src_dir.iterdir()):
                self.src_dir.rmdir()
                print("   ✅ Removed empty src/ directory")
        except Exception as e:
            print(f"   ⚠️  Could not remove src/ directory: {e}")
        
        print()
        print(f"✅ Cleared {cleared_count} practice day(s)!")
        print("   Ready for a fresh start.")
        
        return 0
    
    def clear_specific_day(self, day_num: int, confirm: bool = True) -> int:
        """Clear a specific day directory"""
        day_dir = self.src_dir / f"day{day_num}"
        
        if not day_dir.exists():
            print(f"❌ Day {day_num} not found.")
            print(f"   Directory does not exist: {day_dir}")
            return 1
        
        print(f"🗑️  Found practice day to clear:")
        print(f"   📁 {day_dir}")
        print()
        
        if confirm:
            response = input(f"❓ Are you sure you want to delete day {day_num}? (y/N): ")
            if response.lower() not in ['y', 'yes']:
                print("❌ Clear operation cancelled.")
                return 1
        
        try:
            shutil.rmtree(day_dir)
            print(f"✅ Cleared day {day_num}!")
        except Exception as e:
            print(f"❌ Error clearing day {day_num}: {e}")
            return 1
        
        return 0
    
    def list_days(self) -> int:
        """List all existing practice days"""
        day_dirs = self.find_day_directories()
        
        if not day_dirs:
            print("📭 No practice days found.")
            print("   Run 'python scripts/generate.py' to create your first day.")
            return 0
        
        print(f"📚 Found {len(day_dirs)} practice day(s):")
        for day_dir in day_dirs:
            day_num = int(day_dir.name[3:])
            
            # Count algorithm files
            py_files = list(day_dir.glob("*.py"))
            # Exclude __init__.py from count
            algo_files = [f for f in py_files if f.name != "__init__.py"]
            
            print(f"   📁 Day {day_num}: {len(algo_files)} algorithm(s)")
        
        print()
        print("Commands:")
        print("   python scripts/clear.py --all     # Clear all days")
        print("   python scripts/clear.py --day N   # Clear specific day")
        
        return 0


def main():
    """Main function with command line argument parsing"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Clear generated practice folders",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scripts/clear.py                    # List existing days
  python scripts/clear.py --all              # Clear all days
  python scripts/clear.py --day 3            # Clear day 3
  python scripts/clear.py --all --no-confirm # Clear all without confirmation
        """
    )
    
    parser.add_argument(
        "--all", 
        action="store_true", 
        help="Clear all practice days"
    )
    
    parser.add_argument(
        "--day", 
        type=int, 
        metavar="N",
        help="Clear specific day number"
    )
    
    parser.add_argument(
        "--no-confirm", 
        action="store_true",
        help="Skip confirmation prompt"
    )
    
    args = parser.parse_args()
    
    print("🧹 Python Kata-Machine Clearer")
    print("=" * 40)
    
    clearer = KataClearer()
    confirm = not args.no_confirm
    
    if args.all:
        return clearer.clear_all_days(confirm=confirm)
    elif args.day is not None:
        return clearer.clear_specific_day(args.day, confirm=confirm)
    else:
        return clearer.list_days()


if __name__ == "__main__":
    sys.exit(main())
