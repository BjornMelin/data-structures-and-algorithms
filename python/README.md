# Python Implementations 🐍

> Clean and efficient implementations of data structures and algorithms in Python, emphasizing readability and Pythonic design patterns.

## 📑 Table of Contents

- [🔧 Requirements](#requirements)
- [📦 Setup](#setup)
- [📁 Project Structure](#project-structure)
- [✅ Testing](#testing)
- [📝 Style Guide](#style-guide)
- [📚 Documentation](#documentation)
- [📊 Minimum Code Coverage](#minimum-code-coverage)
- [📜 Google-Style Docstring Template](#google-style-docstring-template)
- [💬 In-Function Comment Requirements](#in-function-comment-requirements)
- [📄 Standardized README.md Template](#standardized-readme-template)

## 🔧 Requirements

- Python 3.8 or higher
- pytest (testing framework)
- black (code formatter)
- mypy (optional static type checking)

## 📦 Setup

```bash
# Navigate to Python directory
cd python

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest

# Format code
black .

# Type checking (optional)
mypy .
```

## 📁 Project Structure

```plaintext
python/
├── algorithms/
│   ├── sorting/
│   │   ├── bubble_sort/
│   │   ├── bucket_sort/
│   │   ├── counting_sort/
│   │   ├── heap_sort/
│   │   ├── insertion_sort/
│   │   ├── merge_sort/
│   │   ├── quick_sort/
│   │   ├── radix_sort/
│   │   ├── selection_sort/
│   │   └── tim_sort/
│   └── searching/
│       ├── binary_search/
│       ├── exponential_search/
│       ├── fibonacci_search/
│       ├── hash_based_search/
│       ├── interpolation_search/
│       ├── jump_search/
│       ├── linear_search/
│       └── ternary_search/
├── tests/
│   └── algorithms/
│       ├── searching/
│       │   ├── test_binary_search.py
│       │   ├── test_exponential_search.py
│       │   ├── test_fibonacci_search.py
│       │   ├── test_hash_based_search.py
│       │   ├── test_interpolation_search.py
│       │   ├── test_jump_search.py
│       │   ├── test_linear_search.py
│       │   └── test_ternary_search.py
│       └── sorting/
│           ├── test_bubble_sort.py
│           ├── test_bucket_sort.py
│           ├── test_counting_sort.py
│           ├── test_heap_sort.py
│           ├── test_insertion_sort.py
│           ├── test_merge_sort.py
│           ├── test_quick_sort.py
│           ├── test_radix_sort.py
│           ├── test_selection_sort.py
│           └── test_tim_sort.py
├── benchmarks/
│   ├── search_benchmark_results.md
│   └── sort_benchmark_results.md
├── requirements.txt
└── setup.py
```

## ✅ Testing

All implementations include comprehensive unit tests using pytest:

```python
def test_quick_sort_random_array():
    """Test quicksort with a random array of integers."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    assert quick_sort(arr) == expected
```

## 📝 Style Guide

- Follow PEP 8 guidelines
- Use snake_case for functions and variables
- Use PascalCase for class names
- Include type hints (Python 3.8+)
- Maximum line length: 88 characters (Black default)

Example:

```python
from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class BinarySearchTree(Generic[T]):
    """
    Implements a generic Binary Search Tree data structure.

    Attributes:
        root: The root node of the tree
    """

    def __init__(self) -> None:
        self.root: Optional[Node[T]] = None

    def insert(self, element: T) -> bool:
        """
        Insert a new element into the tree.

        Args:
            element: The element to insert

        Returns:
            bool: True if insertion was successful

        Raises:
            ValueError: If element is None
        """
        if element is None:
            raise ValueError("Element cannot be None")
        # Implementation details...
```

## 📚 Documentation

### Common Operations Complexity

| Algorithm            | Time Complexity (Best) | Time Complexity (Average) | Time Complexity (Worst) | Space Complexity |
| -------------------- | ---------------------- | ------------------------- | ----------------------- | ---------------- |
| Linear Search        | O(1)                   | O(n)                      | O(n)                    | O(1)             |
| Binary Search        | O(1)                   | O(log n)                  | O(log n)                | O(1)             |
| Jump Search          | O(1)                   | O(√n)                     | O(√n)                   | O(1)             |
| Interpolation Search | O(1)                   | O(log log n)              | O(n)                    | O(1)             |
| Exponential Search   | O(1)                   | O(log n)                  | O(log n)                | O(1)             |
| Fibonacci Search     | O(1)                   | O(log n)                  | O(log n)                | O(1)             |
| Ternary Search       | O(1)                   | O(log n)                  | O(log n)                | O(1)             |
| Hash-based Search    | O(1)                   | O(1)                      | O(1)                    | O(1)             |
| Quick Sort           | O(n log n)             | O(n log n)                | O(n²)                   | O(log n)         |
| Merge Sort           | O(n log n)             | O(n log n)                | O(n log n)              | O(n)             |
| Heap Sort            | O(n log n)             | O(n log n)                | O(n log n)              | O(1)             |
| Bubble Sort          | O(n)                   | O(n²)                     | O(n²)                   | O(1)             |
| Selection Sort       | O(n²)                  | O(n²)                     | O(n²)                   | O(1)             |
| Insertion Sort       | O(n)                   | O(n²)                     | O(n²)                   | O(1)             |
| Radix Sort           | O(nk)                  | O(nk)                     | O(nk)                   | O(n + k)         |
| Counting Sort        | O(n + k)               | O(n + k)                  | O(n + k)                | O(k)             |
| Bucket Sort          | O(n + k)               | O(n + k)                  | O(n²)                   | O(n + k)         |
| Tim Sort             | O(n)                   | O(n log n)                | O(n log n)              | O(n)             |

### Implementation Notes

- Emphasis on Pythonic implementations
- Type hints used throughout the codebase
- Generator patterns used where appropriate
- Context managers implemented where relevant
- Comprehensive docstrings following Google style

### Performance Tips

- Using `collections` for specialized data structures
- Leveraging built-in Python functions
- List comprehensions over explicit loops
- Proper use of generators for memory efficiency

## 📊 Minimum Code Coverage

All code must have a minimum of 90% test coverage. This ensures that the code is well-tested and reliable.

## 📜 Google-Style Docstring Template

All functions and methods should use the following Google-style docstring template:

```python
def example_function(param1: int, param2: str) -> bool:
    """
    Brief description of the function.

    Args:
        param1 (int): Description of param1.
        param2 (str): Description of param2.

    Returns:
        bool: Description of the return value.

    Raises:
        ValueError: Description of the exception raised.

    Time Complexity:
        Best Case: O(1) - Description of the best case.
        Average Case: O(n) - Description of the average case.
        Worst Case: O(n^2) - Description of the worst case.

    Space Complexity: O(1) - Description of the space complexity.

    Examples:
        >>> example_function(1, "example")
        True
    """
    pass
```

## 💬 In-Function Comment Requirements

In-function comments should be used to explain critical steps of the algorithm, including:

- Algorithm step explanations
- Time/space complexity annotations for critical operations
- Edge case handling explanations

Example:

```python
def binary_search(arr: list[int], target: int) -> int:
    """
    Perform a binary search on the given sorted list to find the target element.

    Args:
        arr (list): The sorted list to search through.
        target: The element to search for.

    Returns:
        int: The index of the target element if found, otherwise -1.

    Raises:
        ValueError: If the input list is empty.

    Time Complexity:
        Best Case: O(1) - When the target is at the middle position.
        Average Case: O(log n) - When the target is somewhere in the list.
        Worst Case: O(log n) - When the target is at the last position or not present.

    Space Complexity: O(1) - Only a constant amount of extra space is used.

    Examples:
        >>> binary_search([1, 2, 3, 4, 5], 3)
        2
        >>> binary_search([1, 2, 3, 4, 5], 6)
        -1
    """
    if not arr:
        raise ValueError("Input list cannot be empty")

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

## 📄 Standardized README.md Template

Each data structure and algorithm implementation should have a README.md file with the following sections:

1. **Overview and Purpose**: A brief description of the data structure or algorithm and its purpose.
2. **API Documentation**: A table with the time and space complexity of the main operations.
3. **Usage Examples**: Code snippets demonstrating how to use the data structure or algorithm.
4. **Implementation Details**: Detailed explanation of the algorithm or data structure, including pseudocode.
5. **Mermaid Diagrams**: Visual representation of the algorithm or data structure using Mermaid diagrams.
6. **Performance Benchmarks**: Results of performance benchmarks with methodology.
7. **Comparison with Python's Built-in Equivalents**: Comparison with Python's built-in data structures or algorithms, if applicable.

Example:

```markdown
# Binary Search Algorithm

## Overview and Purpose

Binary Search is an efficient algorithm for finding a target value within a sorted array. It works by repeatedly dividing the search interval in half, making it much faster than linear search for large datasets.

## API Documentation

| Operation | Time Complexity | Space Complexity |
| --------- | ---------------- | ---------------- |
| Search    | O(log n)         | O(1)             |

## Usage Examples

```python
from binary_search import binary_search

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target)
print(f"Element {target} found at index: {result}")
```

## Implementation Details

1. Start with a sorted array
2. Find the middle element of the array
3. If the target value is equal to the middle element, return its index
4. If the target value is less than the middle element, repeat the search on the left half
5. If the target value is greater than the middle element, repeat the search on the right half
6. Continue this process until the target is found or determined to be not in the array

## Mermaid Diagrams

```mermaid
graph TD
    A[Start] --> B[Initialize left = 0, right = length - 1]
    B --> C{left ≤ right?}
    C -- Yes --> D[Calculate mid = left + (right - left) // 2]
    D --> E{A[mid] = target?}
    E -- Yes --> F[Return mid]
    E -- No --> G{A[mid] < target?}
    G -- Yes --> H[left = mid + 1]
    G -- No --> I[right = mid - 1]
    H --> C
    I --> C
    C -- No --> J[Return -1]
    F --> K[End]
    J --> K
```

## Performance Benchmarks

| Test Case         | Input          | Expected Output | Actual Output |
| ----------------- | -------------- | --------------- | ------------- |
| Element at start  | [1,2,3,4,5], 1 | 0               | 0             |
| Element in middle | [1,2,3,4,5], 3 | 2               | 2             |
| Element at end    | [1,2,3,4,5], 5 | 4               | 4             |
| Element not found | [1,2,3,4,5], 6 | -1              | -1            |
| Empty list        | [], 1          | -1              | -1            |
| Single element    | [1], 1         | 0               | 0             |

## Comparison with Python's Built-in Equivalents

Python's built-in `bisect` module provides similar functionality for binary search. However, the custom implementation allows for more flexibility and customization.
```
```
