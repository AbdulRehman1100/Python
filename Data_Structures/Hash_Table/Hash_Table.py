from functions import is_prime, next_prime

class Node:
    def __init__(self, key = None, data = None):
        self._key = key
        self._data = data
        self._next = None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, key):
        self._key = key

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, next):
        self._next = next


class HashTable:
    def __init__(self, size):
        self._table_size = size if is_prime(size) else next_prime(size)
        self._table = [Node()] * self._table_size

    def add(self, key, data):
        index = hash(key) % self._table_size
        print(index)
        new_node = Node(key, data)
        new_node.next = self._table[index]
        self._table[index] = new_node