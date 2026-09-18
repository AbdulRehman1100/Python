class MinHeap:
    '''
    Standard MinHeap with insert(), build_heap(), remove(), extract_min(), get_min(), is_empty(), decrease_key, increase_key and read only current_size property.

    - __lt__ method must defined for the user defined class otherwise raises TypeError.
    - 1-based indexed, means indexes ranges from 1 to current size.
    - Heap will resize by 2 * current capacity if current capacity == current size on insert.
    - Similarly, heap will reize 2 * current capacity if current capacity < size of input array.
    '''
    def __init__(self, capacity = 100):
        '''
        Raises TypeError if capacity is non-integer
        Raises ValueError if capacity is non-positive
        '''
        if type(capacity) is not int:
            raise TypeError("Capacity must be an integer")
        if capacity < 1:
            raise ValueError("Capacity must be positive")
        
        self._capacity = capacity
        self._array = [None] * (capacity + 1)
        self._current_size = 0

    def insert(self, x):
        '''
        Insert x in the heap.
        '''
        if self._current_size == self._capacity:
            self._resize()

        self._current_size += 1
        self._array[self._current_size] = x
        hole = self._current_size

        # heapify the hole up
        self._percolate_up(hole)

    def _percolate_down(self, hole):
        temp = self._array[hole]

        while hole * 2 <= self._current_size:
            child = hole * 2
            if child != self._current_size and self._array[child + 1] < self._array[child]:
                child += 1
            if self._array[child] < temp:
                self._array[hole] = self._array[child]
                hole = child
            else:
                break
        self._array[hole] = temp

    def extract_min(self):
        '''
        Remove and return minimum element from heap.
        Raises IndexError if called upon empty heap.
        '''
        if self._current_size == 0:
            raise IndexError("Cannot extract from an empty heap")
        
        min_item = self._array[1]
        self._array[1] = self._array[self._current_size]
        self._current_size -= 1
        self._percolate_down(1)
        return min_item

    def is_empty(self):
        return self._current_size == 0

    def build_heap(self, array):
        '''
        Build heap from elements provided in the array.
        '''
        while len(array) > self._capacity:
            self._resize()

        for i in range(len(array)):
            self._array[i+1] = array[i]

        self._current_size = len(array)
        i = len(array)//2
        while i > 0:
            self._percolate_down(i)
            i -= 1

    def _resize(self):
        self._capacity *= 2
        new_array = [None] * (self._capacity + 1)
        for i in range(1, self._current_size + 1):
            new_array[i] = self._array[i]
        self._array = new_array

    def get_min(self):
        '''
        Return minimum element from heap.
        Raises IndexError if called upon empty heap.
        '''
        if self._current_size == 0:
            raise IndexError("Cannot extract from an empty heap")
        return self._array[1]

    def _percolate_up(self, hole):
        temp = self._array[hole]

        while hole > 1 and temp < self._array[hole//2]:
            self._array[hole] = self._array[hole//2]
            hole = hole//2 
        self._array[hole] = temp

    def decrease_key(self, index, delta):
        '''
        Decrease key/element at index by delta.

        Raises IndexError if index <= 0 or greater than current size of the heap.
        Raise ValueError if delta is negative.
        '''
        if index <= 0:
            raise IndexError("Index must be positive")
        if index > self._current_size:
             raise IndexError("Index out of range")
        
        if delta < 0:
            raise ValueError("Delta must be non-negative")
        self._array[index] -= delta
        self._percolate_up(index)

    def increase_key(self, index, delta):
        '''
        Increase key/element at index by delta.

        Raises IndexError if index <= 0 or greater than current size of the heap.
        Raise ValueError if delta is negative.
        '''
        if index <= 0:
            raise IndexError("Index must be positive")
        if index > self._current_size:
             raise IndexError("Index out of range")
        
        if delta < 0:
            raise ValueError("Delta must be non-negative")
        self._array[index] += delta
        self._percolate_down(index)

    def remove(self, index):
        '''
        Remove key/element at index.

        Raises IndexError if index <= 0 or greater than current size of the heap.
        '''
        if index <= 0:
            raise IndexError("Index must be positive")
        if index > self._current_size:
             raise IndexError("Index out of range")

        self._array[index] = self._array[self._current_size]
        self._current_size -= 1
        if index > 1 and self._array[index] < self._array[index//2]:
            self._percolate_up(index)
        else:
            self._percolate_down(index)

    @property
    def current_size(self):
        return self._current_size