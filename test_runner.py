#!/usr/bin/env python3
"""
Test runner for Python Kata-Machine
Equivalent to 'yarn test' in the original kata-machine
"""

import sys
import subprocess
from pathlib import Path
from typing import Optional, List
import importlib.util

from config_loader import ConfigLoader


class KataTestRunner:
    """Test runner for kata algorithms"""
    
    def __init__(self, base_dir: Path = None):
        self.base_dir = base_dir or Path.cwd()
        self.src_dir = self.base_dir / "src"
        self.tests_dir = self.base_dir / "tests"
        self.config_loader = ConfigLoader()
    
    def find_latest_day(self) -> Optional[int]:
        """Find the latest day directory"""
        # Look for day directories in current directory (not src/)
        day_dirs = []
        for item in self.base_dir.iterdir():
            if item.is_dir() and item.name.startswith("day"):
                try:
                    day_num = int(item.name[3:])
                    day_dirs.append(day_num)
                except ValueError:
                    continue
        
        return max(day_dirs) if day_dirs else None
    
    def run_tests_for_day(self, day_num: int, verbose: bool = True) -> int:
        """Run tests for a specific day"""
        day_dir = self.base_dir / f"day{day_num}"
        
        if not day_dir.exists():
            print(f"❌ Day {day_num} not found at {day_dir}")
            print("   Run 'python kata.py daily' to generate today's practice")
            return 1
        
        # Add the day directory to Python path for imports
        day_dir_str = str(day_dir)
        if day_dir_str not in sys.path:
            sys.path.insert(0, day_dir_str)
        
        print(f"🧪 Testing Day {day_num} Algorithm")
        print("=" * 50)
        
        # Get algorithm files in the day directory
        algo_files = [f for f in day_dir.glob("*.py") if f.name != "__init__.py"]
        if not algo_files:
            print(f"❌ No algorithm files found in {day_dir}")
            return 1
        
        # Run pytest on specific test files for this day's algorithms
        test_files = []
        for algo_file in algo_files:
            algo_name = algo_file.stem  # filename without .py
            test_file = self.tests_dir / f"test_{algo_name}.py"
            if test_file.exists():
                test_files.append(str(test_file))
        
        if not test_files:
            print(f"⚠️  No test files found for day {day_num} algorithms")
            print("   Your algorithm files exist but no corresponding tests were found")
            print("   This means the algorithm isn't covered in our test examples yet")
            return 0
        
        pytest_args = [
            "python", "-m", "pytest"
        ] + test_files + [
            "-v" if verbose else "-q",
            "--tb=short",
            "--color=yes"
        ]
        
        try:
            result = subprocess.run(pytest_args, cwd=str(self.base_dir))
            return result.returncode
        except FileNotFoundError:
            print("❌ pytest not found. Make sure pytest is installed.")
            return 1
    
    def run_tests_latest_day(self, verbose: bool = True) -> int:
        """Run tests for the latest generated day"""
        latest_day = self.find_latest_day()
        
        if latest_day is None:
            print("❌ No practice days found.")
            print("   Run 'python scripts/generate.py' to create your first day.")
            return 1
        
        print(f"🎯 Running tests for latest day: Day {latest_day}")
        return self.run_tests_for_day(latest_day, verbose)
    
    def run_specific_algorithm_test(self, algorithm_name: str, day_num: Optional[int] = None) -> int:
        """Run tests for a specific algorithm"""
        if day_num is None:
            day_num = self.find_latest_day()
            if day_num is None:
                print("❌ No practice days found.")
                return 1
        
        print(f"🧪 Testing {algorithm_name} (Day {day_num})")
        print("=" * 50)
        
        # Convert algorithm name to test file pattern
        test_pattern = f"**/test_{self._to_snake_case(algorithm_name)}.py"
        
        pytest_args = [
            "python", "-m", "pytest",
            str(self.tests_dir),
            "-k", self._to_snake_case(algorithm_name),
            "-v",
            "--tb=short",
            f"--day={day_num}",
            "--color=yes"
        ]
        
        try:
            result = subprocess.run(pytest_args, cwd=str(self.base_dir))
            return result.returncode
        except FileNotFoundError:
            print("❌ pytest not found. Make sure pytest is installed.")
            return 1
    
    def list_available_tests(self) -> int:
        """List all available test files"""
        if not self.tests_dir.exists():
            print("❌ Tests directory not found.")
            print("   Tests will be automatically created when you generate algorithms.")
            return 1
        
        test_files = list(self.tests_dir.glob("test_*.py"))
        
        if not test_files:
            print("📭 No test files found.")
            return 0
        
        print(f"🧪 Available Tests ({len(test_files)} algorithms):")
        for test_file in sorted(test_files):
            algorithm_name = test_file.stem[5:]  # Remove 'test_' prefix
            print(f"   📄 {algorithm_name}")
        
        return 0
    
    def _to_snake_case(self, name: str) -> str:
        """Convert CamelCase to snake_case"""
        result = []
        for i, char in enumerate(name):
            if char.isupper() and i > 0:
                result.append('_')
            result.append(char.lower())
        return ''.join(result)


def main():
    """Main function with command line argument parsing"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Run tests for Python Kata-Machine algorithms",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python test_runner.py                     # Test latest day
  python test_runner.py --day 2             # Test specific day
  python test_runner.py --algorithm QuickSort  # Test specific algorithm
  python test_runner.py --list              # List available tests
        """
    )
    
    parser.add_argument(
        "--day", 
        type=int, 
        metavar="N",
        help="Test specific day number"
    )
    
    parser.add_argument(
        "--algorithm", 
        type=str, 
        metavar="NAME",
        help="Test specific algorithm"
    )
    
    parser.add_argument(
        "--list", 
        action="store_true",
        help="List available tests"
    )
    
    parser.add_argument(
        "--quiet", 
        action="store_true",
        help="Run tests quietly"
    )
    
    args = parser.parse_args()
    
    print("🧪 Python Kata-Machine Test Runner")
    print("=" * 50)
    
    # Find kata-machine root directory (where kata.py exists)
    kata_root = Path(__file__).parent
    while kata_root != kata_root.parent and not (kata_root / "kata.py").exists():
        kata_root = kata_root.parent

    runner = KataTestRunner(kata_root)
    verbose = not args.quiet
    
    if args.list:
        return runner.list_available_tests()
    elif args.algorithm:
        return runner.run_specific_algorithm_test(args.algorithm, args.day)
    elif args.day is not None:
        return runner.run_tests_for_day(args.day, verbose)
    else:
        return runner.run_tests_latest_day(verbose)


if __name__ == "__main__":
    sys.exit(main())
