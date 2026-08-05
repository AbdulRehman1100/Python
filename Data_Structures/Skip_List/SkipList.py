import random
# TowerNode
class Node:
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
    Max_level = 30
    def __init__(self, min, max):
        self._head = Node(SkipList.Max_level, min)
        self._tail = Node(SkipList.Max_level, max)

        for level in range(len(self._head)):
            self._head[level] = self._tail

    def __search_predecessor(self, data):
        predecessors = [None] * len(self._head)
        current = self._head

        for level in range(len(self._head) - 1, -1, -1):
            while current[level].data < data:
                current = current[level]
            predecessors[level] = current

        return predecessors

    def __random_level(self):
        level = 0
        result = random.choice((0,1))
        while result == 1 and level < SkipList.Max_level:
            level += 1
            result = random.choice((0,1))

        return level

    def insert(self, data):
        update = self.__search_predecessor(data)
        node_height = self.__random_level()
        new_node = Node(node_height, data)

        for level in range(node_height + 1):
            new_node[level] = update[level][level]
            update[level][level] = new_node