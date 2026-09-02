class DisjointSets:
    def __init__(self, n):
        self._parent = [-1] * n


    # find path compression
    def find(self, x):
        if self._parent[x] < 0:
            return x
        else:
            self._parent[x] = self.find(self._parent[x])
            return self._parent[x]
    

    # union by size/weight
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self._parent[root_x] <= self._parent[root_y]:
                self._parent[root_x] += self._parent[root_y]
                self._parent[root_y] = root_x
                return root_x
            else:
                self._parent[root_y] += self._parent[root_x]
                self._parent[root_x] = root_y
                return root_y

    def connected(self, x, y):
        return self.find(x) == self.find(y)