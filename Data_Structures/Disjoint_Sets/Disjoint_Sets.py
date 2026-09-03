class DisjointSets:
    '''
    Standard Disjoint Sets (Union-Find) with union by size and path compression.

    - Elements are represented by integer indices from 0 to n-1.
    - Each set is a tree; the root's stored value is the negative size
      of that set (e.g. -3 means the set has 3 elements).
    '''
    def __init__(self, n):
        '''
        Create n disjoint sets, each containing a single element (0 to n-1).

        Raises TypeError if n is not an integer.
        Raises ValueError if n is less than 1.
        '''
        ...
        if type(n) is not int:
            raise TypeError("n must be an integer")
        if n < 1:
            raise ValueError("n must be positive")
        
        self._parent = [-1] * n
        self._no_of_elements = n - 1 # 0-based indexed

    def _validate_element(self, x):
        '''
        Raises TypeError if x is not an integer.
        Raises ValueError if x is out of range (not between 0 and n-1).
        '''
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be non-negative")
        if x > self._no_of_elements:
             raise ValueError(f"x must be between 0 and {self._no_of_elements}")

    # find path compression
    def find(self, x):
        '''
        Return the root (representative) of the set containing x.

        Applies path compression: every node visited during the search
        is re-parented directly to the root, speeding up future calls.

        Raises TypeError/ValueError via validation if x is invalid.
        '''
        ...
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
        '''
        Merge the sets containing x and y.

        Uses union by size: the smaller set's root is attached under
        the larger set's root, and the larger root's size is updated.

        Return the resulting common root (whether or not a merge
        actually happened — if x and y were already in the same set,
        their existing common root is returned).

        Raises TypeError/ValueError via validation if x or y is invalid.
        '''
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
    
        return root_x  # already same set, return existing common root

    def connected(self, x, y):
        '''
        Return True if x and y are in the same set, otherwise False.

        Raises TypeError/ValueError via validation if x or y is invalid.
        '''
        self._validate_element(x)
        self._validate_element(y)
        return self.find(x) == self.find(y)