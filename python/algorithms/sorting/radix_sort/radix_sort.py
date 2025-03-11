"""
Radix Sort Algorithm Implementation
Author: Bjorn Melin
Date: 1/28/2025

Radix Sort is a non-comparative sorting algorithm that sorts integers by processing individual digits. 
It processes digits from the least significant to the most significant (LSD Radix Sort).

Time Complexity:
- Best Case: O(nk)
- Average Case: O(nk)
- Worst Case: O(nk)

Space Complexity: O(n + k)
"""

from typing import List


def counting_sort_for_radix(arr: List[int], exp: int) -> List[int]:
    """
    A function to do counting sort of arr[] according to the digit represented by exp.

    Args:
        arr (List[int]): The list of integers to be sorted.
        exp (int): The exponent representing the digit position (1 for units, 10 for tens, etc.).

    Returns:
        List[int]: The partially sorted list of integers.

    Raises:
        TypeError: If the input is not a list of integers or if exp is not an integer.

    Time Complexity:
        Best Case: O(n)
        Average Case: O(n)
        Worst Case: O(n)

    Space Complexity: O(n + k)

    Examples:
        >>> counting_sort_for_radix([170, 45, 75, 90, 802, 24, 2, 66], 1)
        [170, 90, 802, 2, 24, 45, 75, 66]
        >>> counting_sort_for_radix([170, 45, 75, 90, 802, 24, 2, 66], 10)
        [802, 2, 24, 45, 66, 170, 75, 90]
    """
    if not isinstance(arr, list) or not all(isinstance(i, int) for i in arr):
        raise TypeError("Input must be a list of integers")
    if not isinstance(exp, int):
        raise TypeError("exp must be an integer")

    n = len(arr)
    output = [0] * n  # output array
    count = [0] * 10  # count array for digits (0 to 9)

    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that count[i] now contains actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]

    return arr


def radix_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array of integers using the Radix Sort algorithm.

    Args:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list of integers.

    Raises:
        TypeError: If the input is not a list of integers.

    Time Complexity:
        Best Case: O(nk)
        Average Case: O(nk)
        Worst Case: O(nk)

    Space Complexity: O(n + k)

    Examples:
        >>> radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
        [2, 24, 45, 66, 75, 90, 170, 802]
        >>> radix_sort([5, 1, 4, 2, 8])
        [1, 2, 4, 5, 8]
    """
    if not isinstance(arr, list) or not all(isinstance(i, int) for i in arr):
        raise TypeError("Input must be a list of integers")

    # Find the maximum number to know the number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead of passing digit number, exp is passed.
    # exp is 10^i where i is the current digit number
    exp = 1
    while max1 // exp > 0:
        arr = counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr
