from BST import BST
import pytest

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

def test_search_min():
    t = BST()
    # empty BST
    with pytest.raises(ValueError):
        t.search_min()

    t.insert(50)
    t.insert(30)
    t.insert(70)
    t.insert(10)
    t.insert(80)

    # non empty BST
    assert t.search_min() == 10

def test_delete_empty_BST():
    t = BST()
    # empty BST
    assert t.delete(10) == False

def test_delete_leaf_node():
    t = BST()
    t.insert(50)
    t.insert(30)
    t.insert(70)
    assert t.delete(30) == True
    assert t.inorder() == [50, 70]

def test_delete_node_with_one_child():
    t = BST()
    t.insert(50)
    t.insert(30)
    t.insert(20)
    assert t.delete(30) == True
    assert t.inorder() == [20, 50]

def test_delete_node_with_two_child():
    t = BST()
    t.insert(50)
    t.insert(30)
    t.insert(70)
    t.insert(60)
    t.insert(80)
    assert t.delete(70) == True
    assert t.inorder() == [30, 50, 60, 80]

def test_delete_non_existent():
    t = BST()
    t.insert(50)
    t.insert(30)
    t.insert(70)
    t.insert(60)
    t.insert(80)
    assert t.delete(99) == False
    assert t.inorder() == [30, 50, 60, 70, 80]

def test_delete_root():
    t = BST()
    t.insert(50)
    assert t.delete(50) == True
    assert t._root is None

def test_delete_root_with_children():
    t = BST()
    t.insert(50)
    t.insert(30)
    t.insert(70)
    assert t.delete(50) == True
    assert t.inorder() == [30, 70]
    assert t._root.object == 70  # inorder successor (min of right subtree) becomes new root