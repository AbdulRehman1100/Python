class DisjointSets:
    def __init__(self, n):
        self._parent = [-1] * n

    def find(self, x):
        while self._parent[x] >= 0:
            x = self._parent[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self._parent[root_y] = root_x
        return root_x

    def connected(self, x, y):
        return self.find(x) == self.find(y)

# ds = DisjointSets(5)
# print(ds.find(0))  # expect 0
# print(ds.find(3))  # expect 3

ds = DisjointSets(5)
print(ds.find(0))  # 0
print(ds.find(1))  # 1
ds.union(0, 1)
print(ds.find(0))  # ?
print(ds.find(1))  # ?