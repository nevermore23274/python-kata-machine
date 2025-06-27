"""
Tests for Linear Search algorithm
Based on ThePrimeagen's kata-machine test cases
"""

import pytest
from typing import List, Optional


@pytest.mark.search
def test_linear_search_basic(import_algorithm):
    """Test basic linear search functionality"""
    linear_search = import_algorithm("LinearSearch")
    
    # Test finding existing elements
    haystack = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    
    assert linear_search(haystack, 69) == True
    assert linear_search(haystack, 1337) == True
    assert linear_search(haystack, 69420) == True
    assert linear_search(haystack, 1) == True
    assert linear_search(haystack, 99) == True


def test_linear_search_not_found(import_algorithm):
    """Test linear search when element is not found"""
    linear_search = import_algorithm("LinearSearch")
    
    haystack = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    
    assert linear_search(haystack, 0) == False
    assert linear_search(haystack, 2) == False
    assert linear_search(haystack, 100) == False
    assert linear_search(haystack, 69421) == False


def test_linear_search_edge_cases(import_algorithm):
    """Test linear search edge cases"""
    linear_search = import_algorithm("LinearSearch")
    
    # Empty array
    assert linear_search([], 1) == False
    
    # Single element - found
    assert linear_search([42], 42) == True
    
    # Single element - not found
    assert linear_search([42], 1) == False
    
    # First element
    haystack = [1, 2, 3, 4, 5]
    assert linear_search(haystack, 1) == True
    
    # Last element
    assert linear_search(haystack, 5) == True


def test_linear_search_duplicates(import_algorithm):
    """Test linear search with duplicate elements"""
    linear_search = import_algorithm("LinearSearch")
    
    haystack = [1, 2, 3, 2, 4, 2, 5]
    
    # Should find duplicate elements
    assert linear_search(haystack, 2) == True
    assert linear_search(haystack, 1) == True
    assert linear_search(haystack, 5) == True
    assert linear_search(haystack, 6) == False


def test_linear_search_type_consistency(import_algorithm):
    """Test that linear search works with different types consistently"""
    linear_search = import_algorithm("LinearSearch")
    
    # String array
    string_haystack = ["apple", "banana", "cherry", "date"]
    assert linear_search(string_haystack, "banana") == True
    assert linear_search(string_haystack, "grape") == False
    
    # Mixed types should work if implementation is generic
    # Note: This depends on the specific implementation
    # Some implementations might be type-specific
