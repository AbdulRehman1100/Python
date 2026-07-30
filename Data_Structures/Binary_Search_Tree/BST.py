class TreeNode:
    def __init__(self, object = None):
        self._object = object
        self._left = None
        self._right = None

    @property
    def object(self):
        return self._object

    @object.setter
    def object(self, object):
        self._object = object

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left_node):
        self._left = left_node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right_node):
        self._right = right_node

class BST:
    '''
    Standard BST with insert(), delete(), preorder(), inorder(), postorder(), search() and search_min().

    - Can store any type of data(homogeneous/heterogeneous)
    - Duplicated data is not allowed.
    - <, > and = operators must be overloaded for the user defined class otherwise TypeError will raise
      while calling method on BST instances.
    '''
    def __init__(self):
        self._root = None

    def insert(self, object):
        '''
        Insert the object in left subtree if object < root's object or 
        in right subtree if object > root object's recursively.

        - Duplicate object will not be insert.
        - Return True except for duplicated data.
        '''
        self._root, success = self._insert_helper(self._root, object)
        return success
        
    def _insert_helper(self, node, object):
        if node is None:
            return (TreeNode(object), True)
        elif object < node.object:
            node.left, success = self._insert_helper(node.left, object)
        elif object > node.object:
            node.right, success = self._insert_helper(node.right, object)
        else:
            return (node, False)
        return (node, success)

    def preorder(self):
        '''
        Return list of objects in preoreder.

        - Empty list on empty tree.
        '''
        result = []
        self._preorder_helper(self._root, result)
        return result

    def _preorder_helper(self, node, result):
        if node is not None:
            result.append(node.object)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)

    def inorder(self):
        '''
        Return list of objects in inoreder.

        - Empty list on empty tree.
        '''
        result = []
        self._inorder_helper(self._root, result)
        return result

    def _inorder_helper(self, node, result):
        if node is not None:
            self._inorder_helper(node.left, result)
            result.append(node.object)
            self._inorder_helper(node.right, result)

    def postorder(self):
        '''
        Return list of objects in postoreder.

        - Empty list on empty tree.
        '''
        result = []
        self._postorder_helper(self._root, result)
        return result

    def _postorder_helper(self, node, result):
        if node is not None:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.object)

    def search(self, object):
        '''
        Return True/False
        '''
        return self._search_helper(self._root, object)

    def _search_helper(self, node, object):
        if node is None:
            return False
        elif object < node.object:
            success = self._search_helper(node.left, object)
        elif object > node.object:
            success = self._search_helper(node.right, object)
        else:
            success = True
            
        return success

    def search_min(self):
        '''
        Return minimum object in the whole BST.

        - Raises ValueError if called upon empty tree.
        '''
        if self._root is None:
            raise ValueError("Cannot find minimum of an empty tree")
        return self._search_min_helper(self._root).object
    
    def _search_min_helper(self, node):
        if node.left is None:
            return node
        return self._search_min_helper(node.left)

    def delete(self, object):
        '''
        Delete the object in the BST if match.
        
        - Return False if the tree is empty (object cannot be found).
        '''
        self._root, success = self._delete_helper(self._root, object)
        return success

    def _delete_helper(self, node, object):
        # base case where match is not in the BST
        if node is None:
            return (node, False)
        # traverse respective branch to found match
        if object < node.object:
            node.left, success = self._delete_helper(node.left, object)
        elif object > node.object:
            node.right, success = self._delete_helper(node.right, object)
        # handle the case if the node to be deleted have both child
        elif node.left is not None and node.right is not None:
            min_node = self._search_min_helper(node.right)
            node.object = min_node.object
            node.right, success = self._delete_helper(node.right, min_node.object)
        else:
            # handle the case if the node to be deleted have only one child
            if node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            # handle the case if the node to be deleted have no child
            else:
                node = None
            success = True

        return (node, success)