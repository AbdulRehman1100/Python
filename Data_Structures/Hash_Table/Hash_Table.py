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
        self._table = [Node() for _ in range(self._table_size)] # dummy header node(key=None, data=None) list

    def add(self, key, data):
        index = hash(key) % self._table_size

        node = self._table[index]
        while node.key != key and node.next is not None: # traverse to either matching key node or end of the list
           node = node.next

        if node.key == key: # update data of duplicate key
            node.data = data
        else:
            node.next = Node(key, data) # append new key, data pair at end

    def get(self, key):
        index = hash(key) % self._table_size
        node = self._table[index]
        while node is not None:
            if node.key == key:
                return node.data
            node = node.next
        return None