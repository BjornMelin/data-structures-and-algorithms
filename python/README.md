# Python Implementations 🐍

> Clean and efficient implementations of data structures and algorithms in Python, emphasizing readability and Pythonic design patterns.

## 📑 Table of Contents

- [🔧 Requirements](#requirements)
- [📦 Setup](#setup)
- [📁 Project Structure](#project-structure)
- [✅ Testing](#testing)
- [📝 Style Guide](#style-guide)
- [📚 Documentation](#documentation)

## 🔧 Requirements

- Python 3.8 or higher
- pytest (testing framework)
- black (code formatter)
- mypy (optional static type checking)
- pylint (code linting)
- pytest-cov (test coverage reporting)

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

# Run tests with coverage reporting
pytest --cov=python/ --cov-report=xml

# Format code
black .

# Lint code
pylint python/

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

---

For more details, check the [main documentation](../README.md).
