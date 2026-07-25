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


class Queue:
    '''
    Standard queue with enqueue(), dequeue(), front(), is_empty() and read only size property.

    Build upon linklist with no capacity limit.
    Initially queue would be empty.
    '''
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, value): # add new element at the end of linkedlist
        '''
        Places the provided value/data at the end of queue.
        '''
        new_node = Node(value)

        if self._head is None:
            self._tail = new_node
            self._head = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def dequeue(self): # remove element from front of linkedlist as it takes O(1)
        '''
        Return and remove value/data at the front of queue.

        Raises AttributeError if dequeue is called on empty queue.
        '''
        x = self._head.data
        self._head = self._head.next

        self._size -= 1
        return x

    def front(self):
        '''
        Return value/data at front of queue without removing it.

        Raises AttributeError if front is called on empty queue.
        '''
        return self._head.data

    def is_empty(self):
        '''
        Return true if queue is empty otherwise false
        '''
        return self._head is None

    @property 
    def size(self):
        '''
        Return current size of queue.

        Return integer
        '''
        return self._size
    
    def __str__(self):
        '''
        Return formatted string of values/data of queue.
                
        e.g. Head -> 10 -> 20 -> 30 -> Tail
        Empty string for empty queue.
        '''
        if self._head is None:
            return ""

        elements = ["Head"]
        current = self._head
        while current is not None:
            elements.append(str(current.data))
            current = current.next

        elements.append("Tail")
        return " -> ".join(elements)