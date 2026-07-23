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
    def __init__(self):
        self._head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self._head
        self._head = new_node

    def pop(self):
        x = self._head.data
        self._head = self._head.next
        return x

    def is_empty(self):
        return self._head is None

    def __str__(self):
        current = self._head

        if current is None:
            return ""

        elements = ["Top"]
        while current is not None:
            elements.append(str(current.data))
            current = current.next

        return " -> ".join(elements)

s = Stack()
print(s)
print(s.is_empty())
s.push(5)
print(s)
print(s.pop())
print(s)
print(s.is_empty())

print("************")
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s)
s.pop()
s.pop()
print(s)
s.pop()
s.pop()
s.pop()
# print(s)