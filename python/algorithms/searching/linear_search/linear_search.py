def linear_search(arr, target):
    """
    Perform a linear search on the given list to find the target element.

    Args:
        arr (list): The list to search through.
        target: The element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.

    Raises:
        ValueError: If the input list is empty.

    Time Complexity:
        Best Case: O(1) - When the target is at the first position.
        Average Case: O(n) - When the target is somewhere in the middle.
        Worst Case: O(n) - When the target is at the last position or not present.

    Space Complexity: O(1) - Only a constant amount of extra space is used.

    Examples:
        >>> linear_search([1, 2, 3, 4, 5], 3)
        2
        >>> linear_search([1, 2, 3, 4, 5], 6)
        -1
    """
    if not arr:
        raise ValueError("Input list cannot be empty")

    for index, element in enumerate(arr):
        if element == target:
            return index
    return -1
