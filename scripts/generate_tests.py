#!/usr/bin/env python3
"""
Generate test files for all algorithms in the configuration
Creates placeholder test files that can be filled in with actual test cases
"""

import sys
from pathlib import Path
from typing import List, Dict

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))
from config_loader import ConfigLoader


class TestFileGenerator:
    """Generates test files for algorithms"""
    
    def __init__(self, base_dir: Path = None):
        self.base_dir = base_dir or Path.cwd()
        self.tests_dir = self.base_dir / "tests"
        self.config_loader = ConfigLoader()
        
        # Algorithm categories for markers
        self.algorithm_categories = {
            "search": ["LinearSearch", "BinarySearchList", "TwoCrystalBalls"],
            "sort": ["BubbleSort", "InsertionSort", "MergeSort", "QuickSort"],
            "data_structure": ["Queue", "Stack", "ArrayList", "SinglyLinkedList", "DoublyLinkedList"],
            "tree": ["BTPreOrder", "BTInOrder", "BTPostOrder", "BTBFS", "CompareBinaryTrees", "DFSOnBST"],
            "graph": ["BFSGraphMatrix", "DFSGraphList", "Dijkstra", "PrimsList"],
            "advanced": ["Trie", "LRU", "Map"]
        }
    
    def _to_snake_case(self, name: str) -> str:
        """Convert CamelCase to snake_case"""
        result = []
        for i, char in enumerate(name):
            if char.isupper() and i > 0:
                result.append('_')
            result.append(char.lower())
        return ''.join(result)
    
    def _get_algorithm_category(self, algorithm: str) -> str:
        """Get the category marker for an algorithm"""
        for category, algorithms in self.algorithm_categories.items():
            if algorithm in algorithms:
                return category
        return "algorithm"  # Default category
    
    def _create_test_template(self, algorithm_name: str) -> str:
        """Create a test file template for an algorithm"""
        snake_name = self._to_snake_case(algorithm_name)
        category = self._get_algorithm_category(algorithm_name)
        
        template = f'''"""
Tests for {algorithm_name} algorithm
Based on ThePrimeagen's kata-machine test cases
"""

import pytest
from typing import List, Optional, Any


@pytest.mark.{category}
def test_{snake_name}_basic(import_algorithm):
    """Test basic {algorithm_name} functionality"""
    {snake_name} = import_algorithm("{algorithm_name}")
    
    # TODO: Implement basic functionality tests
    # Example test structure:
    # result = {snake_name}(test_input)
    # assert result == expected_output
    
    pytest.skip("TODO: Implement {algorithm_name} tests")


def test_{snake_name}_edge_cases(import_algorithm):
    """Test {algorithm_name} edge cases"""
    {snake_name} = import_algorithm("{algorithm_name}")
    
    # TODO: Test edge cases like:
    # - Empty inputs
    # - Single element inputs
    # - Boundary conditions
    # - Invalid inputs
    
    pytest.skip("TODO: Implement {algorithm_name} edge case tests")


def test_{snake_name}_performance(import_algorithm):
    """Test {algorithm_name} performance characteristics"""
    {snake_name} = import_algorithm("{algorithm_name}")
    
    # TODO: Add performance tests
    # - Time complexity validation
    # - Space complexity validation
    # - Large input handling
    
    pytest.skip("TODO: Implement {algorithm_name} performance tests")


# TODO: Add algorithm-specific test cases
# Refer to ThePrimeagen's course for the exact test cases and expectations
# Each algorithm should have comprehensive tests covering:
# - Basic functionality
# - Edge cases
# - Error conditions
# - Performance characteristics
# - Algorithm-specific requirements
'''
        return template
    
    def generate_all_test_files(self) -> int:
        """Generate test files for all configured algorithms"""
        try:
            config = self.config_loader.load_config()
            algorithms = config["dsa"]
        except Exception as e:
            print(f"❌ Error loading configuration: {e}")
            return 1
        
        # Create tests directory
        self.tests_dir.mkdir(exist_ok=True)
        
        print(f"🧪 Generating test files for {len(algorithms)} algorithms...")
        
        generated_count = 0
        skipped_count = 0
        
        for algorithm in algorithms:
            test_filename = f"test_{self._to_snake_case(algorithm)}.py"
            test_file_path = self.tests_dir / test_filename
            
            if test_file_path.exists():
                print(f"   ⏭️  Skipped {test_filename} (already exists)")
                skipped_count += 1
                continue
            
            # Generate test file content
            test_content = self._create_test_template(algorithm)
            
            # Write test file
            with open(test_file_path, 'w') as f:
                f.write(test_content)
            
            print(f"   📄 Created {test_filename}")
            generated_count += 1
        
        # Create __init__.py for tests package
        init_file = self.tests_dir / "__init__.py"
        if not init_file.exists():
            init_file.write_text('"""Test package for Python Kata-Machine"""\n')
            print(f"   📄 Created __init__.py")
        
        print()
        print(f"✅ Test generation complete!")
        print(f"   📄 Generated: {generated_count} test files")
        print(f"   ⏭️  Skipped: {skipped_count} existing files")
        print()
        print("Next steps:")
        print("1. Implement actual test cases in the generated test files")
        print("2. Use 'python test_runner.py' to run tests")
        print("3. Refer to ThePrimeagen's course for specific test expectations")
        
        return 0


def main():
    """Main function"""
    print("🧪 Python Kata-Machine Test Generator")
    print("=" * 50)
    
    generator = TestFileGenerator()
    return generator.generate_all_test_files()


if __name__ == "__main__":
    sys.exit(main())
