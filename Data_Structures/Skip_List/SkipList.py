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
    DEFAULT_MAX_LEVEL = 30
    def __init__(self, min_value, max_value, max_level = None):
        self._max_level = (
            max_level if max_level is not None
            else SkipList.DEFAULT_MAX_LEVEL
        )
        self._head = Node(self._max_level, min_value)
        self._tail = Node(self._max_level, max_value)

        for level in range(len(self._head)):
            self._head[level] = self._tail

    def _search_predecessor(self, data):
        predecessors = [None] * len(self._head)
        current = self._head

        for level in range(len(self._head) - 1, -1, -1):
            while current[level].data < data:
                current = current[level]
            predecessors[level] = current

        return predecessors

    def _random_level(self):
        level = 0
        result = random.choice((0,1))
        while result == 1 and level < self._max_level:
            level += 1
            result = random.choice((0,1))

        return level

    def insert(self, data):
        update = self._search_predecessor(data)
        node_height = self._random_level()
        new_node = Node(node_height, data)

        for level in range(node_height + 1):
            new_node[level] = update[level][level]
            update[level][level] = new_node

    def __str__(self):
        lines = []

        for level in range(self._max_level - 1, -1, -1):
            current = self._head
            elements = []
            while current[level].data != self._tail.data:
                current = current[level]
                elements.append(str(current.data))
            if elements:  # sirf woh levels dikhao jinme koi element ho
                lines.append(f"Level {level}: " + " -> ".join(elements))

        return "\n".join(lines)

    def get_level_0_items(self):
        LEVEL_0 = 0
        elements = []

        current = self._head
        while current[LEVEL_0].data != self._tail.data:
            current = current[LEVEL_0]
            elements.append(current.data)

        return elements

    def search(self, data):
        current = self._head

        for level in range(len(self._head) - 1, -1, -1):
            while current[level].data < data:
                current = current[level]

        if current[0].data == data:
                return current[0]
        
        return None

    def remove(self, data):
        current = self._head
        remove_status = False

        for level in range(len(self._head) - 1, -1, -1):
            while current[level].data < data:
                current = current[level]

            if current[level].data == data:
                current[level] = current[level][level]
                remove_status = True

        return remove_status