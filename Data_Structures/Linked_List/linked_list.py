
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
    
    def __str__(self):
        elements = []
        current = self.head.next
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)
    
    def move(self):
        if self.current.next is not None:
            self.current = self.current.next
            return True
        else:
            self.current = None
            return False
    
    def find(self, value):
        current = self.head.next
        while current is not None:
            if value == current.data:
                return current
            current = current.next
        return None