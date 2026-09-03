class DisjointSets:
    def __init__(self, n):
        if type(n) is not int:
            raise TypeError("n must be an integer")
        if n < 1:
            raise ValueError("n must be positive")
        
        self._parent = [-1] * n
        self._no_of_elements = n - 1 # 0-based indexed

    def _validate_element(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be non-negative")
        if x > self._no_of_elements:
             raise ValueError(f"x must be between 0 and {self._no_of_elements}")

    # find path compression
    def find(self, x):
        self._validate_element(x)
        return self._find_helper(x)

    def _find_helper(self, x):
        if self._parent[x] < 0:
            return x
        else:
            self._parent[x] = self._find_helper(self._parent[x])
            return self._parent[x]
    

    # union by size/weight
    def union(self, x, y):
        self._validate_element(x)
        self._validate_element(y)

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
        self._validate_element(x)
        self._validate_element(y)
        return self.find(x) == self.find(y)