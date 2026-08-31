from Disjoint_Sets import DisjointSets

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

def test_find_no_union():
    ds = DisjointSets(5)
    assert ds.find(0) == 0
    assert ds.find(3) == 3

def test_find_after_union():
    ds = DisjointSets(5)
    ds.union(0, 1)
    assert ds.find(1) == ds.find(0)
    