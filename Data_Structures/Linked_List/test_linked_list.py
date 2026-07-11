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