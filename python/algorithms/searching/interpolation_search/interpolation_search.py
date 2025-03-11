from typing import List, Any


def interpolation_search(arr: List[Any], target: Any) -> int:
    """
    Perform an interpolation search on the given sorted list to find the target element.

    Args:
        arr (List[Any]): The sorted list to search through.
        target (Any): The element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.

    Raises:
        ValueError: If the input list is empty.

    Time Complexity:
        Best Case: O(1) - When the target is at the estimated position.
        Average Case: O(log log n) - When the target is somewhere in the list.
        Worst Case: O(n) - When the target is uniformly distributed and not present.

    Space Complexity: O(1) - Only a constant amount of extra space is used.

    Examples:
        >>> interpolation_search([1, 2, 3, 4, 5], 3)
        2
        >>> interpolation_search([1, 2, 3, 4, 5], 6)
        -1
    """
    if not arr:
        raise ValueError("Input list cannot be empty")

    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        pos = low + int(
            ((float(high - low) / (arr[high] - arr[low])) * (target - arr[low]))
        )

        if arr[pos] == target:
            return pos
        if arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1
