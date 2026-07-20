from linked_list import LinkedList

def test_add_single():
    ll = LinkedList()
    ll.add(1)
    assert ll.head.next.data == 1
    assert ll.head.next.next is None

def test_add_multiple():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    assert ll.head.next.data == 1
    assert ll.head.next.next.data == 2
    assert ll.head.next.next.next.data == 3
    assert ll.head.next.next.next.next is None

def test_empty_list():
    ll = LinkedList()
    assert ll.head.next is None

def test_current_pointer():
    ll = LinkedList()
    assert ll.current is None
    ll.add(1)
    ll.add(2)
    ll.add(3)
    assert ll.current.data == 3
    assert ll.current.next is None

def test_str_empty_list():
    ll = LinkedList()
    assert str(ll) == ""

def test_str_single_element():
    ll = LinkedList()
    ll.add(1)
    assert str(ll) == "1"

def test_str_multiple_elements():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    assert str(ll) == "1 -> 2 -> 3"

def test_start_empty_list():
    ll = LinkedList()
    ll.start()
    assert ll.current is None

def test_start_non_empty_list():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.start()
    assert ll.current.data == 1

def test_move_success():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.start()
    
    result = ll.move()
    assert result == True
    assert ll.current.data == 2

def test_move_at_end():
    ll = LinkedList()
    ll.add(1)
    ll.start()
    
    result = ll.move()
    assert result == False
    assert ll.current.data == 1

def test_move_empty_list():
    ll = LinkedList()
    result = ll.move()
    
    assert result == False
    assert ll.current is None

def test_find_success():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    assert ll.find(3).data == 3

def test_find_failure():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.add(4)
    ll.add(5)
    assert ll.find(9) is None

def test_find_empty_list():
    ll = LinkedList()
    assert ll.find(5) is None

def test_remove_at_start():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.start()  # current = Node(1)
    assert ll.remove() ==  True
    assert ll.current.data == 2

def test_remove_at_end():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)  # current = Node(3)
    assert ll.remove() ==  True
    assert ll.current is None

def test_remove_at_middle():
    ll = LinkedList()
    ll.add(1)
    ll.add(2)
    ll.add(3)
    ll.start()
    ll.move()  # current = Node(2)
    assert ll.remove() ==  True
    assert ll.current.data == 3

def test_remove_empty_list():
    ll = LinkedList()  # current = None
    assert ll.remove() ==  False
    assert ll.current is None


def test_remove_single_element_list():
    ll = LinkedList()
    ll.add(1)
    ll.start()  # current = Node(1)
    assert ll.remove() == True
    assert ll.current is None
    assert str(ll) == ""

def test_remove_twice():
    ll = LinkedList()
    ll.add(1)
    ll.start()
    ll.remove()  # now list is empty
    assert ll.remove() == False  # calling remove again, shouldn't do anyting
    assert ll.current is None