from MinHeap import MinHeap

def test_insert_and_extract_sorted_order():
    h = MinHeap()
    h.insert(10)
    h.insert(5)
    h.insert(20)
    h.insert(3)
    
    assert h.extract_min() == 3
    assert h.extract_min() == 5
    assert h.extract_min() == 10
    assert h.extract_min() == 20

def test_insert_and_extract_single_element():
    h = MinHeap()
    h.insert(99)
    assert h.extract_min() == 99

def test_insert_and_extract_duplicate_elements():
    h = MinHeap()
    h.insert(10)
    h.insert(10)
    h.insert(5)
    h.insert(20)
    h.insert(3)
    h.insert(7)
    h.insert(7)

    assert h.extract_min() == 3
    assert h.extract_min() == 5
    assert h.extract_min() == 7
    assert h.extract_min() == 7
    assert h.extract_min() == 10
    assert h.extract_min() == 10
    assert h.extract_min() == 20

def test_is_empty():
    h = MinHeap()
    assert h.is_empty() == True
    h.insert(5)
    assert h.is_empty() == False
    h.extract_min()
    assert h.is_empty() == True