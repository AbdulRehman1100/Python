
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
    
    def add_after_current(self, value = None):
        new_node = Node(value)

        if self.head.next == None:
            self.head.next = new_node
            self.current = new_node
            self.last_current = self.head
        elif self.current is None:
            raise ValueError("Cursor is not positioned. Call start() first.")
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
    
    def move_next(self):
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

    def remove_current(self):
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
    
    def insert_at(self, value, position):
        if position < 0 or position > self.size:
            raise IndexError
        
        is_empty = self.is_empty()
        saved_current = self.current
        saved_last_current = self.last_current
        
        new_node = Node(value)
        
        if self.head.next is None:
            self.head.next = new_node
            self.last_current = self.head
            self.current = new_node
        else:
            self.current = self.head
            i = 0
            while i < position:
                self.last_current = self.current
                self.current = self.current.next
                i += 1
            
            self.last_current = self.current
            new_node.next = self.current.next
            self.current.next = new_node
        
        if not is_empty:
            self.current = saved_current
            self.last_current = saved_last_current
        self.size += 1

    def remove_by_value(self, value):
        if self.is_empty():
            return False
        
        saved_current = self.current
        saved_last_current = self.last_current
        
        self.current = self.head
        while True:
            if not self.move_next():
                self.current = saved_current
                self.last_current = saved_last_current
                return False
            if self.current.data == value:
                break
        
        was_current = (self.current == saved_current)
        
        self.last_current.next = self.current.next
        self.size -= 1
        
        if was_current:
            self.current = None
            self.last_current = None
        else:
            self.current = saved_current
            self.last_current = saved_last_current
        
        return True
        