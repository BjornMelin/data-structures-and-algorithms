from typing import List, Any


def ternary_search(arr: List[Any], target: Any) -> int:
    """
    Perform a ternary search on the given sorted list to find the target element.

    Args:
        arr (List[Any]): The sorted list to search through.
        target (Any): The element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.

    Raises:
        ValueError: If the input list is empty.

    Time Complexity:
        Best Case: O(1) - When the target is at the first or second division.
        Average Case: O(log3 n) - When the target is somewhere in the list.
        Worst Case: O(log3 n) - When the target is at the last position or not present.

    Space Complexity: O(1) - Only a constant amount of extra space is used.

    Examples:
        >>> ternary_search([1, 2, 3, 4, 5], 3)
        2
        >>> ternary_search([1, 2, 3, 4, 5], 6)
        -1
    """
    if not arr:
        raise ValueError("Input list cannot be empty")

    left, right = 0, len(arr) - 1

    while left <= right:
        third = (right - left) // 3
        mid1 = left + third
        mid2 = right - third

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            right = mid1 - 1
        elif target > arr[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return -1
