class MinHeap:
    def __init__(self, capacity = 100):
        self._capacity = capacity
        self._array = [None] * (capacity + 1)
        self._current_size = 0

    def insert(self, x):
        self._current_size += 1
        hole = self._current_size

        # heapify the hole up
        while hole > 1 and x < self._array[hole//2]:
            self._array[hole] = self._array[hole//2]
            hole = hole//2
        self._array[hole] = x

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
        min_item = self._array[1]
        self._array[1] = self._array[self._current_size]
        self._current_size -= 1
        self._percolate_down(1)
        return min_item

    def is_empty(self):
        return self._current_size == 0