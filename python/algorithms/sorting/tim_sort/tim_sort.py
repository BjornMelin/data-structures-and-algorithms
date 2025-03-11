"""
Tim Sort Algorithm Implementation
Author: Bjorn Melin
Date: 1/28/2025

Tim Sort is a hybrid sorting algorithm derived from merge sort and insertion sort. 
It is used in Python's built-in sorted() and .sort() methods. Tim Sort divides the 
array into small chunks called "runs" and sorts them using insertion sort, then 
merges the sorted runs using merge sort.

Time Complexity:
- Best Case: O(n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

Space Complexity: O(n)
"""

from typing import List

MIN_RUN = 32


def insertion_sort(arr: List[int], left: int, right: int) -> None:
    """
    Sorts a portion of the array using the Insertion Sort algorithm.

    Args:
        arr (List[int]): The list of integers to be sorted.
        left (int): The starting index of the portion to be sorted.
        right (int): The ending index of the portion to be sorted.

    Raises:
        TypeError: If the input is not a list of integers or if left or right are not integers.

    Time Complexity:
        Best Case: O(n) when the array is already sorted
        Average Case: O(n^2)
        Worst Case: O(n^2)

    Space Complexity: O(1)

    Examples:
        >>> insertion_sort([64, 34, 25, 12, 22, 11, 90], 0, 6)
        [11, 12, 22, 25, 34, 64, 90]
        >>> insertion_sort([5, 1, 4, 2, 8], 0, 4)
        [1, 2, 4, 5, 8]
    """
    if not isinstance(arr, list) or not all(isinstance(i, int) for i in arr):
        raise TypeError("Input must be a list of integers")
    if not isinstance(left, int) or not isinstance(right, int):
        raise TypeError("left and right must be integers")

    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr: List[int], left: int, mid: int, right: int) -> None:
    """
    Merges two sorted portions of the array.

    Args:
        arr (List[int]): The list of integers to be merged.
        left (int): The starting index of the first portion.
        mid (int): The ending index of the first portion.
        right (int): The ending index of the second portion.

    Raises:
        TypeError: If the input is not a list of integers or if left, mid, or right are not integers.

    Time Complexity:
        Best Case: O(n)
        Average Case: O(n)
        Worst Case: O(n)

    Space Complexity: O(n)

    Examples:
        >>> merge([4, 10, 3, 5, 1], 0, 2, 4)
        [1, 3, 4, 5, 10]
        >>> merge([4, 10, 3, 5, 1], 0, 1, 4)
        [1, 3, 4, 5, 10]
    """
    if not isinstance(arr, list) or not all(isinstance(i, int) for i in arr):
        raise TypeError("Input must be a list of integers")
    if not isinstance(left, int) or not isinstance(mid, int) or not isinstance(right, int):
        raise TypeError("left, mid, and right must be integers")

    len1, len2 = mid - left + 1, right - mid
    left_part, right_part = [], []

    for i in range(0, len1):
        left_part.append(arr[left + i])
    for i in range(0, len2):
        right_part.append(arr[mid + 1 + i])

    i, j, k = 0, 0, left

    while i < len1 and j < len2:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len1:
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len2:
        arr[k] = right_part[j]
        j += 1
        k += 1


def tim_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array of integers using the Tim Sort algorithm.

    Args:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list of integers.

    Raises:
        TypeError: If the input is not a list of integers.

    Time Complexity:
        Best Case: O(n)
        Average Case: O(n log n)
        Worst Case: O(n log n)

    Space Complexity: O(n)

    Examples:
        >>> tim_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
        >>> tim_sort([5, 1, 4, 2, 8])
        [1, 2, 4, 5, 8]
    """
    if not isinstance(arr, list) or not all(isinstance(i, int) for i in arr):
        raise TypeError("Input must be a list of integers")

    n = len(arr)
    for i in range(0, n, MIN_RUN):
        insertion_sort(arr, i, min((i + MIN_RUN - 1), (n - 1)))

    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min((n - 1), (left + size - 1))
            right = min((left + 2 * size - 1), (n - 1))
            if mid < right:
                merge(arr, left, mid, right)
        size *= 2

    return arr
