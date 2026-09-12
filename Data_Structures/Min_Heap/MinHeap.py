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

h = MinHeap()
h.insert(10)
h.insert(5)
h.insert(20)
h.insert(3)
print(h._array[1:h._current_size+1])