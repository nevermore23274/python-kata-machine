"""
Pytest configuration and fixtures for Python Kata-Machine
"""

import sys
import pytest
from pathlib import Path
from typing import Any, Callable, List


def pytest_addoption(parser):
    """Add custom command line options"""
    parser.addoption(
        "--day", 
        action="store", 
        default=None,
        help="Run tests for specific day only"
    )


def pytest_configure(config):
    """Configure pytest with custom markers"""
    # Add day directories to Python path for imports
    base_dir = Path(__file__).parent.parent
    
    # Find day directories in base directory (not src/)
    day_dirs = [d for d in base_dir.iterdir() if d.is_dir() and d.name.startswith("day")]
    if day_dirs:
        latest_day = max(day_dirs, key=lambda x: int(x.name[3:]))
        sys.path.insert(0, str(latest_day))
        print(f"🔧 Added {latest_day} to Python path for testing")


def pytest_collection_modifyitems(config, items):
    """Modify test collection based on command line options"""
    day_option = config.getoption("--day")
    
    if day_option:
        # Filter tests to only run for specified day
        day_marker = f"day{day_option}"
        selected_items = []
        
        for item in items:
            # Check if test has the day marker or if no day marker is present
            if item.get_closest_marker(day_marker) or not any(
                item.get_closest_marker(f"day{i}") for i in range(1, 10)
            ):
                selected_items.append(item)
        
        items[:] = selected_items


@pytest.fixture
def current_day():
    """Fixture to get the current day number from the latest day directory"""
    base_dir = Path(__file__).parent.parent
    day_dirs = [d for d in base_dir.iterdir() if d.is_dir() and d.name.startswith("day")]
    if not day_dirs:
        return 1
    
    latest_day = max(day_dirs, key=lambda x: int(x.name[3:]))
    return int(latest_day.name[3:])


@pytest.fixture
def import_algorithm():
    """Fixture to dynamically import algorithms from the current day"""
    def _import_algorithm(algorithm_name: str, day: int = None):
        """Import an algorithm function from the specified day"""
        if day is None:
            # Auto-detect latest day in base directory
            base_dir = Path(__file__).parent.parent
            day_dirs = [d for d in base_dir.iterdir() if d.is_dir() and d.name.startswith("day")]
            if day_dirs:
                latest_day = max(day_dirs, key=lambda x: int(x.name[3:]))
                day = int(latest_day.name[3:])
            else:
                day = 1
        
        # Convert algorithm name to module and function name
        module_name = _to_snake_case(algorithm_name)
        function_name = module_name
        
        try:
            # Import from the current day directory 
            base_dir = Path(__file__).parent.parent
            day_dir = base_dir / f"day{day}"
            sys.path.insert(0, str(day_dir))
            module = __import__(f"{module_name}", fromlist=[function_name])
            return getattr(module, function_name)
        except (ImportError, AttributeError) as e:
            pytest.fail(f"Could not import {algorithm_name} from day{day}: {e}")d.name.startswith("day")]
            if day_dirs:
                latest_day = max(day_dirs, key=lambda x: int(x.name[3:]))
                day = int(latest_day.name[3:])
            else:
                day = 1
        
        # Convert algorithm name to module and function name
        module_name = _to_snake_case(algorithm_name)
        function_name = module_name
        
        try:
            # Import from the current day directory 
            sys.path.insert(0, str(latest_day))
            module = __import__(f"{module_name}", fromlist=[function_name])
            return getattr(module, function_name)
        except (ImportError, AttributeError) as e:
            pytest.fail(f"Could not import {algorithm_name} from {latest_day.name}: {e}")
    
    return _import_algorithm


def _to_snake_case(name: str) -> str:
    """Convert CamelCase to snake_case"""
    result = []
    for i, char in enumerate(name):
        if char.isupper() and i > 0:
            result.append('_')
        result.append(char.lower())
    return ''.join(result)


# Common test data fixtures
@pytest.fixture
def sample_arrays():
    """Common arrays for testing sorting and search algorithms"""
    return {
        "empty": [],
        "single": [42],
        "sorted": [1, 2, 3, 4, 5],
        "reverse_sorted": [5, 4, 3, 2, 1],
        "random": [3, 1, 4, 1, 5, 9, 2, 6, 5, 3],
        "duplicates": [1, 3, 2, 3, 1, 2, 3],
        "large": list(range(100, 0, -1))  # 100 elements in reverse order
    }


@pytest.fixture
def sample_strings():
    """Common strings for testing string algorithms"""
    return {
        "empty": "",
        "single_char": "a",
        "simple": "hello",
        "with_spaces": "hello world",
        "repeated": "aabbcc",
        "palindrome": "racecar"
    }


# Performance testing helpers
class TimeComplexityAssertion:
    """Helper class for asserting time complexity"""
    
    @staticmethod
    def assert_linear_or_better(func: Callable, test_sizes: List[int] = None):
        """Assert that function runs in O(n) or better time"""
        # This is a placeholder for more sophisticated timing tests
        # In practice, you'd time the function with different input sizes
        pass
    
    @staticmethod
    def assert_logarithmic_or_better(func: Callable, test_sizes: List[int] = None):
        """Assert that function runs in O(log n) or better time"""
        pass


@pytest.fixture
def time_complexity():
    """Fixture for time complexity assertions"""
    return TimeComplexityAssertion
