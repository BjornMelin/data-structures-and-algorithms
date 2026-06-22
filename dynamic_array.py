import ctypes

class DynamicArray:
    """
    A dynamic array implementation in Python that automatically resizes
    when the capacity is reached.
    
    Time Complexity:
    - append: O(1) amortized
    - insert: O(n)
    - get: O(1)
    - set: O(1)
    - remove: O(n)
    - size: O(1)
    - is_empty: O(1)
    - clear: O(1)
    
    Space Complexity:
    - O(n), where n is the number of elements stored.
    """
    
    def __init__(self, capacity=2):
        """Initialize dynamic array with given capacity."""
        self._n = 0  # Number of elements
        self._capacity = capacity  # Initial capacity
        self._array = self._make_array(self._capacity)
    
    def _make_array(self, capacity):
        """Creates a low-level array with the given capacity."""
        return (capacity * ctypes.py_object)()
    
    def _resize(self, new_capacity):
        """Resizes the array to the new capacity."""
        new_array = self._make_array(new_capacity)
        for i in range(self._n):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity
    
    def append(self, element):
        """Appends an element to the array."""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._array[self._n] = element
        self._n += 1
    
    def insert(self, index, element):
        """Inserts an element at a given index."""
        if not 0 <= index <= self._n:
            raise IndexError("Index out of bounds")
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for i in range(self._n, index, -1):
            self._array[i] = self._array[i - 1]
        self._array[index] = element
        self._n += 1
    
    def get(self, index):
        """Returns the element at the given index."""
        if not 0 <= index < self._n:
            raise IndexError("Index out of bounds")
        return self._array[index]
    
    def set(self, index, element):
        """Updates the element at the given index."""
        if not 0 <= index < self._n:
            raise IndexError("Index out of bounds")
        self._array[index] = element
    
    def remove(self, index):
        """Removes the element at the given index."""
        if not 0 <= index < self._n:
            raise IndexError("Index out of bounds")
        for i in range(index, self._n - 1):
            self._array[i] = self._array[i + 1]
        self._array[self._n - 1] = None
        self._n -= 1
        if self._n > 0 and self._n == self._capacity // 4:
            self._resize(self._capacity // 2)
    
    def size(self):
        """Returns the number of elements in the array."""
        return self._n
    
    def is_empty(self):
        """Checks if the array is empty."""
        return self._n == 0
    
    def clear(self):
        """Clears the array by resetting all elements while preserving the current capacity."""
        self._n = 0
        self._array = self._make_array(self._capacity)
    
    def __iter__(self):
        """Iterator implementation."""
        for i in range(self._n):
            yield self._array[i]
    
    def __str__(self):
        return str([self._array[i] for i in range(self._n)])



if __name__ == "__main__":
    arr = DynamicArray()
    arr.append(1)
    arr.append(2)
    arr.append(3)
    print(arr)  
    arr.insert(1, 5)
    print(arr)  
    arr.remove(2)
    print(arr)  
