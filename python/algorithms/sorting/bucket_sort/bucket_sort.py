"""
Bucket Sort Algorithm Implementation
Author: Bjorn Melin
Date: 1/28/2025

Bucket Sort is a distribution sort algorithm that works by distributing the elements 
of an array into a number of buckets. Each bucket is then sorted individually, either 
using a different sorting algorithm or by recursively applying the bucket sort algorithm.

Time Complexity:
- Best Case: O(n + k) where k is the number of buckets
- Average Case: O(n + k)
- Worst Case: O(n^2) when all elements are placed in a single bucket

Space Complexity: O(n + k)
"""

from typing import List


def bucket_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array of integers using the Bucket Sort algorithm.

    Args:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list of integers.

    Raises:
        TypeError: If the input is not a list of integers.

    Time Complexity:
        Best Case: O(n + k) where k is the number of buckets
        Average Case: O(n + k)
        Worst Case: O(n^2) when all elements are placed in a single bucket

    Space Complexity: O(n + k)

    Examples:
        >>> bucket_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
        >>> bucket_sort([5, 1, 4, 2, 8])
        [1, 2, 4, 5, 8]
    """
    if not isinstance(arr, list) or not all(isinstance(i, int) for i in arr):
        raise TypeError("Input must be a list of integers")

    if len(arr) == 0:
        return arr

    # Determine minimum and maximum values
    min_value = min(arr)
    max_value = max(arr)

    # Initialize buckets
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Distribute input array values into buckets
    for i in range(len(arr)):
        index = int((arr[i] - min_value) / (max_value - min_value + 1) * bucket_count)
        buckets[index].append(arr[i])

    # Sort each bucket and concatenate the results
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array
