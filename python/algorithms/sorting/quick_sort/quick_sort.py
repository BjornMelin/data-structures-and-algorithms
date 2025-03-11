"""
Quick Sort Algorithm Implementation
Author: Bjorn Melin
Date: 1/28/2025

Quick Sort is a divide-and-conquer algorithm that selects a pivot element 
and partitions the array into two sub-arrays, according to whether they 
are less than or greater than the pivot. The sub-arrays are then sorted 
recursively.

Time Complexity:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n^2)

Space Complexity: O(log n)
"""

from typing import List


def quick_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array of integers using the Quick Sort algorithm.

    Args:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list of integers.

    Raises:
        TypeError: If the input is not a list of integers.

    Time Complexity:
        Best Case: O(n log n)
        Average Case: O(n log n)
        Worst Case: O(n^2)

    Space Complexity: O(log n)

    Examples:
        >>> quick_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
        >>> quick_sort([5, 1, 4, 2, 8])
        [1, 2, 4, 5, 8]
    """
    if not isinstance(arr, list) or not all(isinstance(i, int) for i in arr):
        raise TypeError("Input must be a list of integers")

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
