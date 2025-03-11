"""
Counting Sort Algorithm Implementation
Author: Bjorn Melin
Date: 1/28/2025

Counting Sort is an integer sorting algorithm that operates by counting the 
number of objects that have distinct key values (kind of hashing). It is not 
a comparison-based sorting algorithm and its time complexity is O(n + k), 
where n is the number of elements in the input array and k is the range of 
the input.

Time Complexity:
- Best Case: O(n + k)
- Average Case: O(n + k)
- Worst Case: O(n + k)

Space Complexity: O(n + k)
"""

from typing import List


def counting_sort(arr: List[int]) -> List[int]:
    """
    Sorts an array of integers using the Counting Sort algorithm.

    Args:
        arr (List[int]): The list of integers to be sorted.

    Returns:
        List[int]: The sorted list of integers.

    Raises:
        TypeError: If the input is not a list of integers.

    Time Complexity:
        Best Case: O(n + k)
        Average Case: O(n + k)
        Worst Case: O(n + k)

    Space Complexity: O(n + k)

    Examples:
        >>> counting_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
        >>> counting_sort([5, 1, 4, 2, 8])
        [1, 2, 4, 5, 8]
    """
    if not isinstance(arr, list) or not all(isinstance(i, int) for i in arr):
        raise TypeError("Input must be a list of integers")

    if not arr:
        return []

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    # Initialize count array
    count = [0] * range_of_elements
    output = [0] * len(arr)

    # Store the count of each element
    for num in arr:
        count[num - min_val] += 1

    # Change count[i] so that count[i] now contains the actual
    # position of this element in the output array
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the output array
    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output
