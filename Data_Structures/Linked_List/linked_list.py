
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

class LinkedList:
    def __init__(self):
        self.head = Node()
        self.head.next = None
        self.current = None
    
    def add(self, value = None):
        new_node = Node(value)

        if self.head.next == None:
            self.head.next = new_node
            self.current = new_node
        else:
            self.current.next = new_node
            self.current = new_node

ll = LinkedList()
ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)

print(ll.head.next.data)
print(ll.head.next.next.data)
print(ll.head.next.next.next.data)
print(ll.head.next.next.next.next)