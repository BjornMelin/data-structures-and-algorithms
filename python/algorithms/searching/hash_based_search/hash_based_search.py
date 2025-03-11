from typing import Dict, Any


def hash_based_search(data: Dict[Any, Any], target: Any) -> Any:
    """
    Perform a hash-based search using Python's dictionary to find the target element.

    Args:
        data (Dict[Any, Any]): The dictionary to search through.
        target (Any): The key to search for.

    Returns:
        Any: The value associated with the target key if found, otherwise None.

    Raises:
        ValueError: If the input dictionary is empty.

    Time Complexity:
        Best Case: O(1) - When the target key is found immediately.
        Average Case: O(1) - On average, dictionary lookups are O(1).
        Worst Case: O(1) - In the worst case, dictionary lookups are still O(1).

    Space Complexity: O(1) - Only a constant amount of extra space is used.

    Examples:
        >>> hash_based_search({'a': 1, 'b': 2, 'c': 3}, 'b')
        2
        >>> hash_based_search({'a': 1, 'b': 2, 'c': 3}, 'd')
        None
    """
    if not data:
        raise ValueError("Input dictionary cannot be empty")

    return data.get(target, None)
