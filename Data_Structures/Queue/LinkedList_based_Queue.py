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
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, value): # add new element at the end of linkedlist
        new_node = Node(value)

        if self._head is None:
            self._tail = new_node
            self._head = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def dequeue(self): # remove element from front of linkedlist as it takes O(1)
        x = self._head.data
        self._head = self._head.next

        self._size -= 1
        return x

    def front(self):
        return self._head.data

    def is_empty(self):
        return self._head is None

    @property 
    def size(self):
        return self._size
    
    def __str__(self):
        if self._head is None:
            return ""

        elements = ["Head"]
        current = self._head
        while current is not None:
            elements.append(str(current.data))
            current = current.next

        elements.append("Tail")
        return " -> ".join(elements)

# q = Queue()
# q.enqueue(10)
# q.dequeue()   # single element remove kiya, queue ab empty honi chahiye
# q.enqueue(99)  # naya element add karo
# print(q)

q = Queue()
q.enqueue(10)
q.dequeue()
q.enqueue(20)
q.enqueue(30)
print(q)  # expect: Head -> 20 -> 30 -> Tail
q.dequeue()
q.dequeue()
print(q)  # expect: ""
q.enqueue(99)
print(q)  # expect: Head -> 99 -> Tail — yeh tail ko dobara test karega