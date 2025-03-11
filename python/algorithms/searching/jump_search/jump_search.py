import math
from typing import List, Any


def jump_search(arr: List[Any], target: Any) -> int:
    """
    Perform a jump search on the given sorted list to find the target element.

    Args:
        arr (List[Any]): The sorted list to search through.
        target (Any): The element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.

    Raises:
        ValueError: If the input list is empty.

    Time Complexity:
        Best Case: O(1) - When the target is at the first position.
        Average Case: O(√n) - When the target is somewhere in the list.
        Worst Case: O(√n) - When the target is at the last position or not present.

    Space Complexity: O(1) - Only a constant amount of extra space is used.

    Examples:
        >>> jump_search([1, 2, 3, 4, 5], 3)
        2
        >>> jump_search([1, 2, 3, 4, 5], 6)
        -1
    """
    if not arr:
        raise ValueError("Input list cannot be empty")

    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Finding the block where the target element is present
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search within the block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1

    if arr[prev] == target:
        return prev

    return -1
