from BST import BST

def test_insert_empty_tree():
    t = BST()
    assert t.insert(50) == True
    assert t._root.object == 50
    assert t._root.right is None
    assert t._root.left is None

def test_insert_left_branch():
    t = BST()
    t.insert(50)
    assert t.insert(30) == True
    assert t._root.left.object == 30
    assert t._root.left.left is None
    assert t._root.left.right is None

def test_insert_right_branch():
    t = BST()
    t.insert(50)
    t.insert(30)
    assert t.insert(70) == True
    assert t._root.right.object == 70
    assert t._root.right.left is None
    assert t._root.right.right is None

def test_insert_duplicate():
    t = BST()
    t.insert(50)
    assert t.insert(50) == False
    assert t._root.left is None
    assert t._root.right is None

    t.insert(30)
    t.insert(70)
    assert t.insert(50) == False
    assert t.insert(30) == False
    assert t.insert(70) == False

def test_preorder():
    t = BST()
    # empty BST
    assert t.preorder() == []

    # BST containing single node
    t.insert(50)
    assert t.preorder() == [50]

    # BST containing multiple nodes
    t.insert(30)
    t.insert(70)
    t.insert(10)
    t.insert(80)
    assert t.preorder() == [50, 30, 10, 70, 80]

def test_inorder():
    t = BST()
    # empty BST
    assert t.inorder() == []

    # BST containing single node
    t.insert(50)
    assert t.inorder() == [50]

    # BST containing multiple nodes
    t.insert(30)
    t.insert(70)
    t.insert(10)
    t.insert(80)
    assert t.inorder() == [10, 30, 50, 70, 80]

def test_postorder():
    t = BST()
    # empty BST
    assert t.postorder() == []

    # BST containing single node
    t.insert(50)
    assert t.postorder() == [50]

    # BST containing multiple nodes
    t.insert(30)
    t.insert(70)
    t.insert(10)
    t.insert(80)
    assert t.postorder() == [10, 30, 80, 70, 50]

def test_search():
    t = BST()
    # empty BST
    assert t.search(50) == False

    t.insert(50)
    t.insert(30)
    t.insert(70)
    t.insert(10)
    t.insert(80)
    
    # root match
    assert t.search(50) == True
    # left branch match
    assert t.search(10) == True
    # right branch match
    assert t.search(70) == True

    # match not found
    assert t.search(99) == False