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
    '''
    Standard hash table with add(), remove(), get() methods.
    - Takes mandatory size argument while intilization.
    - If size is not a prime number, then size will automatically be the next prime number for the given number.
    - Raises TypeError if size not a integer
    - Raises ValueError if size non positive
    '''
    def __init__(self, size):
        if type(size) != int:
            raise TypeError("Table size must be an integer")
        if size < 1:
            raise ValueError("Table size can't be non positive")
        
        self._table_size = size if is_prime(size) else next_prime(size)
        self._table = [Node() for _ in range(self._table_size)] # dummy header node(key=None, data=None) list

    def add(self, key, data):
        '''
        Add the key, data pair in the table.
        - Duplicate keys not allowed.
        - Update only only data if key alreay exist.
        - Raises TypeError for key = None.
        '''
        if key is None:
            raise TypeError("Key can't be None")
        
        index = hash(key) % self._table_size
        node = self._table[index]
        while node.key != key and node.next is not None: # traverse to either matching key node or end of the list
           node = node.next

        if node.key == key: # update data of duplicate key
            node.data = data
        else:
            node.next = Node(key, data) # append new key, data pair at end

    def get(self, key):
        '''
        Return the associate with provided key.
        - Return None for non existent key in the table.
        - Raises TypeError for key = None.
        '''
        if key is None:
            raise TypeError("Key can't be None")
        
        index = hash(key) % self._table_size
        node = self._table[index]
        while node is not None:
            if node.key == key:
                return node.data
            node = node.next
        return None

    def remove(self, key):
        '''
        Remove key and associate data from the table.
        - Raises TypeError for key = None.
        '''
        if key is None:
            raise TypeError("Key can't be None")
        
        index = hash(key) % self._table_size
        node = self._table[index]
        prev_node = node # faciliate the delete
        while node.key != key and node.next is not None: # traverse to either matching key node or end of the list
                   prev_node = node
                   node = node.next

        if node.key == key:
            prev_node.next = node.next
            return True
        return False