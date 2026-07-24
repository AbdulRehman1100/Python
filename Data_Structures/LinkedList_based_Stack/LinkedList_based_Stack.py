class Node:
    def __init__(self, data = None):
        self._data = data
        self._next = None

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


class Stack():
    '''
    Standard Stack with push, pop, peek, is_empty, __str__ and size read only property.

    Build upon linkedList with no capacity limit.
    Initially, stack would be empty. 
    '''
    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, value):
        '''Place provided value on the top of Stack.'''
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    def pop(self):
        '''
        Return and remove element on the top of stack.
        
        Raises AttributeError if pop from empty stack.
        '''
        x = self._head.data
        self._head = self._head.next
        self._size -= 1
        return x

    def is_empty(self):
        '''
        Return true if stack is empty otherwise false
        '''
        return self._head is None

    def __str__(self):
        '''
        Return formatted string of elements of stack.
        
        e.g. Top -> 30 -> 20 -> 10
        Empty string for empty stack.
        '''
        current = self._head

        if current is None:
            return ""

        elements = ["Top"]
        while current is not None:
            elements.append(str(current.data))
            current = current.next

        return " -> ".join(elements)

    def peek(self):
        '''
        Return element on the top of stack without removing it.

        Raises AttributeError if peek on empty stack.
        '''
        return self._head.data

    @property
    def size(self):
        '''
        Return current size stack.
        
        Return integer
        '''
        return self._size