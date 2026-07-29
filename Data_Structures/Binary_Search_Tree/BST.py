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

    def search(self, object):
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
        return self._search_min_helper(self._root).object

    def _search_min_helper(self, node):
        if node.left is None:
            return node
        return self._search_min_helper(node.left)

    def delete(self, object):
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

t = BST()
t.insert(50)
t.insert(30)
t.insert(70)
t.insert(60)
t.insert(80)
t.delete(50)  # root ke dono children hain
print(t.inorder())

t2 = BST()
t2.insert(50)
t2.insert(30)
t2.insert(70)
t2.delete(30)
print(t2.inorder())  # expect: [50, 70]

t3 = BST()
t3.insert(50)
t3.insert(30)
t3.insert(20)
t3.delete(30)
print(t3.inorder())  # expect: [20, 50]

t5 = BST()
t5.insert(50)
t5.delete(50)
print(t5._root)  # expect None