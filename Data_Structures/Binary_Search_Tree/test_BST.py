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