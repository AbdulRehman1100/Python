from Disjoint_Sets import DisjointSets

def test_find_no_union():
    ds = DisjointSets(5)
    assert ds.find(0) == 0
    assert ds.find(3) == 3

def test_find_after_union():
    ds = DisjointSets(5)
    ds.union(0, 1)
    assert ds.find(1) == ds.find(0)

def test_find_path_compression():
    ds = DisjointSets(5)
    ds._parent = [1, 2, 3, 4, -4]

    ds.find(0)
    for i in range(4):
        assert ds._parent[i] == 4

def test_union_connects_elements():
    ds = DisjointSets(5)
    ds.union(0, 1)
    assert ds.connected(0, 1) == True
    assert ds.connected(0, 2) == False

def test_union_connects_elements_through_transitivity():
    ds = DisjointSets(5)
    ds.union(0, 1)
    ds.union(1, 2)
    assert ds.connected(0, 2) == True

def test_union_already_connected_pair():
    ds = DisjointSets(5)
    ds.union(0, 1)
    ds.union(0, 1)
    assert ds.connected(0, 1) == True

def test_union_with_self():
    ds = DisjointSets(5)
    ds.union(0, 0)
    assert ds.connected(0, 0) == True

def test_union_by_size_smaller_joins_larger():
    ds = DisjointSets(6)
    ds.union(0, 1)
    ds.union(0, 2)  # set {0,1,2}, size 3, root = 0
    
    ds.union(3, 4)  # set {3,4}, size 2, root = 3
    
    ds.union(0, 3)  # bada (size 3) + chhota (size 2)
    
    # socho: kaunsa root "winner" hona chahiye?
    assert ds.find(3) == 0  # chhota set ka root, bade ke neeche gaya
    assert ds.find(4) == 0  # chhote set ka doosra element bhi ab bade root ke neeche

def test_union_by_size_reverse_order():
    ds = DisjointSets(6)
    ds.union(0, 1)
    ds.union(0, 2)  # set {0,1,2}, size 3
    
    ds.union(3, 4)  # set {3,4}, size 2
    
    ds.union(3, 0)  # chhota (3) union badi (0) ke sath, is baar arguments reverse
    
    assert ds.find(3) == 0  # bhi bade set mein merge hona chahiye