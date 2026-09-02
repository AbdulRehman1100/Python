class DisjointSets:
    def __init__(self, n):
        self._parent = [-1] * n

    def find(self, x):
        while self._parent[x] >= 0:
            x = self._parent[x]
        return x

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


ds = DisjointSets(5)
ds.union(0, 1)
ds.union(0, 2)  # ab set {0,1,2} ka size 3 hai, root 0
ds.union(3, 4)  # set {3,4} ka size 2 hai, root 3

print(ds.union(0, 3))  # bada set (size 3) aur chhota set (size 2) ko union karo