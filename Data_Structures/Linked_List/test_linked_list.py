from linked_list import LinkedList
import pytest

def test_add_after_current_single():
    ll = LinkedList()
    ll.add_after_current(1)
    assert ll.head.next.data == 1
    assert ll.head.next.next is None

def test_add_after_current_multiple():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(2)
    ll.add_after_current(3)
    assert ll.head.next.data == 1
    assert ll.head.next.next.data == 2
    assert ll.head.next.next.next.data == 3
    assert ll.head.next.next.next.next is None

def test_add_after_current_after_move():
    ll = LinkedList()
    ll.add_after_current(10)
    ll.add_after_current(20)
    ll.add_after_current(30)
    ll.start()
    ll.move_next()
    ll.add_after_current(99)
    assert ll.current.data == 99

def test_empty_list():
    ll = LinkedList()
    assert ll.head.next is None

def test_current_pointer():
    ll = LinkedList()
    assert ll.current is None
    ll.add_after_current(1)
    ll.add_after_current(2)
    ll.add_after_current(3)
    assert ll.current.data == 3
    assert ll.current.next is None

def test_str_empty_list():
    ll = LinkedList()
    assert str(ll) == ""

def test_str_single_element():
    ll = LinkedList()
    ll.add_after_current(1)
    assert str(ll) == "1"

def test_str_multiple_elements():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(2)
    ll.add_after_current(3)
    assert str(ll) == "1 -> 2 -> 3"

def test_start_empty_list():
    ll = LinkedList()
    ll.start()
    assert ll.current is None

def test_start_non_empty_list():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(2)
    ll.add_after_current(3)
    ll.start()
    assert ll.current.data == 1

def test_move_next_success():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(2)
    ll.add_after_current(3)
    ll.start()

    result = ll.move_next()
    assert result == True
    assert ll.current.data == 2

def test_move_next_at_end():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.start()

    result = ll.move_next()
    assert result == False
    assert ll.current.data == 1

def test_move_next_empty_list():
    ll = LinkedList()
    result = ll.move_next()

    assert result == False
    assert ll.current is None

def test_find_success():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(2)
    ll.add_after_current(3)
    ll.add_after_current(4)
    ll.add_after_current(5)
    assert ll.find(3).data == 3

def test_find_failure():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(2)
    ll.add_after_current(3)
    ll.add_after_current(4)
    ll.add_after_current(5)
    assert ll.find(9) is None

def test_find_empty_list():
    ll = LinkedList()
    assert ll.find(5) is None

def test_remove_current_at_start():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(2)
    ll.add_after_current(3)
    ll.start()  # current = Node(1)
    assert ll.remove_current() == True
    assert ll.current.data == 2

def test_remove_current_at_end():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(2)
    ll.add_after_current(3)  # current = Node(3)
    assert ll.remove_current() == True
    assert ll.current is None

def test_remove_current_at_middle():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(2)
    ll.add_after_current(3)
    ll.start()
    ll.move_next()  # current = Node(2)
    assert ll.remove_current() == True
    assert ll.current.data == 3

def test_remove_current_empty_list():
    ll = LinkedList()  # current = None
    assert ll.remove_current() == False
    assert ll.current is None

def test_remove_current_single_element_list():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.start()  # current = Node(1)
    assert ll.remove_current() == True
    assert ll.current is None
    assert str(ll) == ""

def test_remove_current_twice():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.start()
    ll.remove_current()  # now list is empty
    assert ll.remove_current() == False  # calling remove again, shouldn't do anything
    assert ll.current is None

def test_len_single_element_list():
    ll = LinkedList()
    ll.add_after_current(1)
    assert len(ll) == 1

def test_len_multiple_elements_list():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(3)
    ll.add_after_current(2)
    assert len(ll) == 3

def test_len_empty_list():
    ll = LinkedList()
    assert len(ll) == 0

def test_len_after_remove():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(3)
    ll.add_after_current(2)
    ll.start()
    ll.remove_current()
    assert len(ll) == 2
    ll.move_next()
    ll.remove_current()
    assert len(ll) == 1
    ll.start()
    ll.remove_current()
    assert len(ll) == 0

def test_is_empty():
    ll = LinkedList()
    assert ll.is_empty() == True
    ll.add_after_current(1)
    assert ll.is_empty() == False
    ll.add_after_current(3)
    ll.add_after_current(2)
    assert ll.is_empty() == False
    ll.remove_current()
    assert ll.is_empty() == False
    ll.start()
    ll.remove_current()
    assert ll.is_empty() == False
    ll.remove_current()
    assert ll.is_empty() == True

def test_insert_at_empty_list():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.insert_at(10, -1)
    with pytest.raises(IndexError):
        ll.insert_at(10, 1)

    ll.insert_at(10, 0)
    assert ll.current.data == 10
    assert len(ll) == 1
    assert ll.head.next.data == 10
    assert ll.current.next == None

def test_insert_at_front():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(3)
    ll.add_after_current(2)

    with pytest.raises(IndexError):
        ll.insert_at(10, -1)
    with pytest.raises(IndexError):
        ll.insert_at(10, 4)

    ll.insert_at(4, 0)
    assert ll.current.data == 2
    assert ll.head.next.data == 4
    assert len(ll) == 4
    assert str(ll) == "4 -> 1 -> 3 -> 2"

def test_insert_at_end():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(3)
    ll.add_after_current(2)

    ll.insert_at(4, 3)
    assert ll.current.data == 2
    assert str(ll) == "1 -> 3 -> 2 -> 4"
    assert len(ll) == 4

def test_insert_at_mid():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(2)
    ll.add_after_current(3)
    ll.add_after_current(4)

    ll.insert_at(99, 2)
    assert ll.current.data == 4
    assert str(ll) == "1 -> 2 -> 99 -> 3 -> 4"
    assert len(ll) == 5

def test_remove_by_value_success():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(2)
    ll.add_after_current(3)
    assert ll.remove_by_value(2) == True
    assert str(ll) == "1 -> 3"
    assert ll.current.data == 3

def test_remove_by_value_failure():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(2)
    ll.add_after_current(3)
    assert ll.remove_by_value(4) == False
    assert str(ll) == "1 -> 2 -> 3"
    assert ll.current.data == 3

def test_remove_by_value_current():
    ll = LinkedList()
    ll.add_after_current(1)
    ll.add_after_current(2)
    ll.add_after_current(3)
    assert ll.remove_by_value(3) == True
    assert str(ll) == "1 -> 2"
    assert ll.current is None

def test_remove_by_value_empty_list():
    ll = LinkedList()
    assert ll.remove_by_value(3) == False
    assert str(ll) == ""
    assert ll.current is None
    assert ll.head.next is None