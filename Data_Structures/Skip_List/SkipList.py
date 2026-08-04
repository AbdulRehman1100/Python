import random
# TowerNode
class Node:
    MAX_LEVELS = 30
    def __init__(self, level_count, data = None):
        self._data = data
        self._next= [None for i in range(level_count + 1)]

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def __getitem__(self, level):
        return self._next[level]
    
    def __setitem__(self, level, node):
        self._next[level] = node

    def __len__(self):
        return len(self._next)

class SkipList:
    def __init__(self, min, max):
        self._head = Node(0, min)
        self._tail = Node(0, max)
        self._head[0] = self._tail

    def insert(self, data):

        no_of_heads = 0
        while random.choice((0,1)) != 0:
            no_of_heads += 1

        levels = no_of_heads
        if no_of_heads >= len(self._head):
            no_of_levels = len(self._head) - no_of_heads
            levels = len(self._head) + no_of_levels
            
        node = Node(levels, data)

        current_node = self._head
        while levels >= 0:
            while data > current_node[levels].data:
                current_node = current_node[levels]

            if data < current_node[levels].data:
                node[levels] = current_node[levels]
                current_node[levels] = node
            levels -= 1

        


# node = Node(1, 5)
# print(node.data)
# print(node[0])

sk = SkipList(-9999, 9999)
sk.insert(10)
sk.insert(20)
print(sk._head.data)
print(sk._head[0].data)
print(sk._head[0][0].data)
print(sk._tail.data)