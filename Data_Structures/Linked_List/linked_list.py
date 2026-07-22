
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

         

# ll = LinkedList()
# ll.add(100)
# ll.add(200)
# ll.add(300)
# ll.insert_at(999, 1)
# print(ll)  # expect: 100 -> 999 -> 200 -> 300

# ll2 = LinkedList()
# ll2.add(100)
# ll2.add(200)
# ll2.add(300)
# ll2.insert_at(999, 2)
# print(ll2)  # expect: 100 -> 200 -> 999 -> 300

# ll4 = LinkedList()
# ll4.add(100)
# ll4.add(200)
# ll4.add(300)
# ll4.insert_at(500, 0)
# print(ll4)  # expect: 100 -> 200 -> 999 -> 300

# ll3 = LinkedList()
# ll3.insert_at(999, 0)  # expect: 999
# ll3.insert_at(500, 1)  # expect: 999
# ll3.insert_at(33, 2)
# print(ll3)

# ll = LinkedList()
# ll.add(100)
# ll.add(200)
# print(len(ll))  # expect 2

# ll.insert_at(999, 1)
# print(len(ll))  # kya expect karte ho? aur kya milta hai?

# ll = LinkedList()
# ll.add(100)
# ll.add(200)
# ll.add(300)
# ll.insert_at(999, 3)
# print(ll)  # expect: 100 -> 200 -> 300 -> 999

l2 = LinkedList()
l2.insert_at(999, 0)
l2.add(10)
print(l2)  # expect: 100 -> 200 -> 300 -> 999

# ll = LinkedList()
# ll.add(1)
# ll.add(2)
# ll.insert_at(99, 1)
# print(ll)
# ll.add(3)
# print(ll)
# ll.start()
# ll.move()
# ll.remove()
# print(ll)