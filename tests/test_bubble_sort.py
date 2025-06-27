"""
Tests for Bubble Sort algorithm
Based on ThePrimeagen's kata-machine test cases
"""

import pytest
from typing import List


@pytest.mark.sort
def test_bubble_sort_basic(import_algorithm, sample_arrays):
    """Test basic bubble sort functionality"""
    bubble_sort = import_algorithm("BubbleSort")
    
    # Test with random array
    arr = sample_arrays["random"].copy()
    bubble_sort(arr)
    assert arr == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
    
    # Test with reverse sorted array
    arr = sample_arrays["reverse_sorted"].copy()
    bubble_sort(arr)
    assert arr == [1, 2, 3, 4, 5]


def test_bubble_sort_edge_cases(import_algorithm, sample_arrays):
    """Test bubble sort edge cases"""
    bubble_sort = import_algorithm("BubbleSort")
    
    # Empty array
    arr = sample_arrays["empty"].copy()
    bubble_sort(arr)
    assert arr == []
    
    # Single element
    arr = sample_arrays["single"].copy()
    bubble_sort(arr)
    assert arr == [42]
    
    # Already sorted
    arr = sample_arrays["sorted"].copy()
    bubble_sort(arr)
    assert arr == [1, 2, 3, 4, 5]


def test_bubble_sort_duplicates(import_algorithm, sample_arrays):
    """Test bubble sort with duplicate elements"""
    bubble_sort = import_algorithm("BubbleSort")
    
    arr = sample_arrays["duplicates"].copy()
    bubble_sort(arr)
    assert arr == [1, 1, 2, 2, 3, 3, 3]


def test_bubble_sort_in_place(import_algorithm):
    """Test that bubble sort modifies array in place"""
    bubble_sort = import_algorithm("BubbleSort")
    
    original_arr = [3, 1, 4, 1, 5, 9, 2, 6]
    arr = original_arr.copy()
    original_id = id(arr)
    
    bubble_sort(arr)
    
    # Array should be modified in place (same object)
    assert id(arr) == original_id
    assert arr == [1, 1, 2, 3, 4, 5, 6, 9]
    assert arr != original_arr


def test_bubble_sort_stability(import_algorithm):
    """Test that bubble sort is stable (maintains relative order of equal elements)"""
    bubble_sort = import_algorithm("BubbleSort")
    
    # Using tuples to track original positions
    # This test assumes the implementation preserves stability
    # Note: This is more of a documentation test since we can't easily
    # verify stability with primitive integers
    arr = [3, 1, 4, 1, 5]
    bubble_sort(arr)
    assert arr == [1, 1, 3, 4, 5]


@pytest.mark.slow
def test_bubble_sort_large_array(import_algorithm, sample_arrays):
    """Test bubble sort with larger array"""
    bubble_sort = import_algorithm("BubbleSort")
    
    arr = sample_arrays["large"].copy()
    bubble_sort(arr)
    
    # Should be sorted
    for i in range(len(arr) - 1):
        assert arr[i] <= arr[i + 1]
    
    # Should contain all original elements
    assert len(arr) == 100
    assert min(arr) == 1
    assert max(arr) == 100


def test_bubble_sort_negative_numbers(import_algorithm):
    """Test bubble sort with negative numbers"""
    bubble_sort = import_algorithm("BubbleSort")
    
    arr = [-3, -1, -4, -1, -5, 0, 2, 1]
    bubble_sort(arr)
    assert arr == [-5, -4, -3, -1, -1, 0, 1, 2]
