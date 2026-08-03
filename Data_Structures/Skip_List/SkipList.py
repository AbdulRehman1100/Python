# TowerNode
class Node:
    MAX_LEVELS = 30
    def __init__(self, level_count, data = None):
        self._data = data
        self._next= [None for i in range(level_count)]

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