from typing import List, Any


def fibonacci_search(arr: List[Any], target: Any) -> int:
    """
    Perform a Fibonacci search on the given sorted list to find the target element.

    Args:
        arr (List[Any]): The sorted list to search through.
        target (Any): The element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.

    Raises:
        ValueError: If the input list is empty.

    Time Complexity:
        Best Case: O(1) - When the target is at the first position.
        Average Case: O(log n) - When the target is somewhere in the list.
        Worst Case: O(log n) - When the target is at the last position or not present.

    Space Complexity: O(1) - Only a constant amount of extra space is used.

    Examples:
        >>> fibonacci_search([1, 2, 3, 4, 5], 1)
        0
        >>> fibonacci_search([1, 2, 3, 4, 5], 3)
        2
        >>> fibonacci_search([1, 2, 3, 4, 5], 5)
        4
        >>> fibonacci_search([1, 2, 3, 4, 5], 6)
        -1
    """
    if not arr:
        raise ValueError("Input list cannot be empty")

    n = len(arr)
    fib_m2 = 0  # (m-2)'th Fibonacci number
    fib_m1 = 1  # (m-1)'th Fibonacci number
    fib_m = fib_m2 + fib_m1  # m'th Fibonacci number

    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_m2, n - 1)

        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i

    if fib_m1 and arr[offset + 1] == target:
        return offset + 1

    return -1
