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
    def __init__(self):
        self._root = None

    def insert(self, object):
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
        result = []
        self._preorder_helper(self._root, result)
        return result

    def _preorder_helper(self, node, result):
        if node is not None:
            result.append(node.object)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)

    def inorder(self):
        result = []
        self._inorder_helper(self._root, result)
        return result

    def _inorder_helper(self, node, result):
        if node is not None:
            self._inorder_helper(node.left, result)
            result.append(node.object)
            self._inorder_helper(node.right, result)

    def postorder(self):
        result = []
        self._postorder_helper(self._root, result)
        return result

    def _postorder_helper(self, node, result):
        if node is not None:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.object)
        



# t = BST()
# t.insert(5)
# print(t._root.object)
# t.insert(10)
# t.insert(4)
# print(t._root.right.object)
# print(t._root.left.object)
# print(t._root.right.right)
# print(t._root.right.left)
# print(t._root.left.right)
# print(t._root.left.left)

t2 = BST()
t2.insert(50)
t2.insert(30)
t2.insert(70)
t2.insert(20)
t2.insert(40)
print(t2.preorder())

print(t2.inorder())
print(t2.postorder())