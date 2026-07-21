
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
        self.last_current = None
        self.size = 0
    
    def add(self, value = None):
        new_node = Node(value)

        if self.head.next == None:
            self.head.next = new_node
            self.current = new_node
            self.last_current = self.head
        else:
            new_node.next = self.current.next
            self.current.next = new_node
            self.last_current = self.current
            self.current = new_node

        self.size += 1
    
    def __str__(self):
        elements = []
        current = self.head.next
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)
    
    def move(self):
        if self.current is not None and self.current.next is not None:
            self.last_current = self.current
            self.current = self.current.next
            return True
        return False
    
    def find(self, value):
        current = self.head.next
        while current is not None:
            if value == current.data:
                return current
            current = current.next
        return None
    
    def start(self):
        self.current = self.head.next
        self.last_current = self.head

    def remove(self):
        if self.current is not None:
            self.last_current.next = self.current.next
            self.current = self.last_current.next
            self.size -= 1
            return True
        
        return False

    def __len__(self):
        return self.size
    
    def is_empty(self):
        if len(self) == 0:
            return True
        return False
    