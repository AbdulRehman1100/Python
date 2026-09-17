from MinHeap import MinHeap
import pytest

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

def test_extract_min_empty_heap():
    h = MinHeap()
    with pytest.raises(IndexError):
        h.extract_min()

def test_build_heap():
    h = MinHeap()
    h.build_heap([10, 5, 20, 3, 7, 1, 15]) 

    assert h.extract_min() == 1
    assert h.extract_min() == 3
    assert h.extract_min() == 5
    assert h.extract_min() == 7
    assert h.extract_min() == 10
    assert h.extract_min() == 15
    assert h.extract_min() == 20

def test_resize_on_insert():
    h = MinHeap(capacity=2)
    h.insert(10)
    h.insert(5)
    h.insert(3)  # yeh resize trigger karega
    assert h.extract_min() == 3
    assert h.extract_min() == 5
    assert h.extract_min() == 10

def test_resize_on_build_heap():
    h = MinHeap(capacity=3)
    h.build_heap([10, 5, 20, 3, 7, 1, 15, 8])
    assert h.extract_min() == 1

def test_get_min_empty_heap():
    h = MinHeap()
    with pytest.raises(IndexError):
        h.get_min()

def test_get_min():
    h = MinHeap()
    h.insert(20)
    h.insert(10)
    h.insert(30)
    h.insert(50)
    h.insert(9)
    h.insert(40)
    assert h.get_min() == 9

def test_decrease_key_index_out_of_range():
    h = MinHeap()
    h.insert(10)
    h.insert(20)
    h.insert(30)
    h.insert(40)
    h.insert(50)

    with pytest.raises(IndexError):
        h.decrease_key(0, 5)
    with pytest.raises(IndexError):
        h.decrease_key(6, 5)

def test_decrease_key_negative_delta():
    h = MinHeap()
    h.insert(10)
    h.insert(20)
    h.insert(30)
    h.insert(40)
    h.insert(50)

    with pytest.raises(ValueError):
        h.decrease_key(3, -2)

def test_decrease_key_through_extract_min():
    h = MinHeap()
    h.insert(10)
    h.insert(20)
    h.insert(30)
    h.insert(40)
    h.insert(50)

    # array[4] is 40 after these inserts
    h.decrease_key(4, 31)
    assert h.extract_min() == 9
    assert h.extract_min() == 10
    assert h.extract_min() == 20
    assert h.extract_min() == 30
    assert h.extract_min() == 50

def test_increase_key_index_out_of_range():
    h = MinHeap()
    h.insert(10)
    h.insert(20)
    h.insert(30)
    h.insert(40)
    h.insert(50)

    with pytest.raises(IndexError):
        h.increase_key(0, 5)
    with pytest.raises(IndexError):
        h.increase_key(6, 5)

def test_increase_key_negative_delta():
    h = MinHeap()
    h.insert(10)
    h.insert(20)
    h.insert(30)
    h.insert(40)
    h.insert(50)

    with pytest.raises(ValueError):
        h.increase_key(3, -2)

def test_increase_key_through_extract_min():
    h = MinHeap()
    h.insert(10)
    h.insert(20)
    h.insert(30)
    h.insert(40)
    h.insert(50)

    # array[2] is 20 after these inserts
    h.increase_key(2, 99)
    assert h.extract_min() == 10
    assert h.extract_min() == 30
    assert h.extract_min() == 40
    assert h.extract_min() == 50
    assert h.extract_min() == 119

def test_remove_index_out_of_range():
    h = MinHeap()
    h.insert(10)
    h.insert(20)
    h.insert(30)
    h.insert(40)
    h.insert(50)

    with pytest.raises(IndexError):
        h.remove(0)
    with pytest.raises(IndexError):
        h.remove(6)

def test_remove():
    h = MinHeap()
    h.insert(10)
    h.insert(20)
    h.insert(30)
    h.insert(40)
    h.insert(50)

    h.remove(3)
    assert h.extract_min() == 10
    assert h.extract_min() == 20
    assert h.extract_min() == 40
    assert h.extract_min() == 50
    
def test_remove_mutliple_elements():
    h = MinHeap()
    h.insert(10)
    h.insert(20)
    h.insert(30)
    h.insert(40)
    h.insert(50)

    h.remove(1)
    h.remove(4)
    assert h.extract_min() == 20
    assert h.extract_min() == 30
    assert h.extract_min() == 40