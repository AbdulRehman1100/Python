from LinkedList_based_Stack import Stack
import pytest

def test_push():
    # empty stack
    s = Stack()
    s.push(10)
    assert s._head.data == 10
    assert s._head.next is None
    assert str(s) == "Top -> 10"

    # non empty stack
    s.push(20)
    assert s._head.data == 20
    assert s._head.next.data == 10
    assert s._head.next.next is None
    assert str(s) == "Top -> 20 -> 10"

    # push after pop
    s.pop()
    s.push(30)
    assert s._head.data == 30
    assert s._head.next is None
    assert str(s) == "Top -> 30 -> 10"


def test_pop():
    # test empty stack
    s = Stack()
    with pytest.raises(AttributeError):
        s.pop()

    # pop from stack containing single element
    s.push(10)
    assert s.pop() == 10
    assert s._head is None

    # pop from stack containing multiple elements
    s.push(10)
    s.push(20)
    s.push(30)
    assert s.pop() == 30
    assert str(s) == "Top -> 20 -> 10"


def test_is_empty():
    # empty stack
    s = Stack()
    assert s.is_empty() == True
    assert str(s) == ""

    # is_empty after push
    s.push(10)
    assert s.is_empty() == False
    assert str(s) == "Top -> 10"
    s.push(20)
    assert s.is_empty() == False
    assert str(s) == "Top -> 20 -> 10"

    # is_empty after pop
    s.pop()
    assert s.is_empty() == False
    assert str(s) == "Top -> 10"
    s.pop()
    assert s.is_empty() == True
    assert str(s) == ""

def test_peek():
    # test empty stack
    s = Stack()
    with pytest.raises(AttributeError):
        s.peek()

    # peek from stack containing single element
    s.push(10)
    assert s.peek() == 10
    assert s._head.data == 10
    assert str(s) == "Top -> 10"

    # pop from stack containing multiple elements
    s.push(20)
    s.push(30)
    assert s.peek() == 30
    assert s._head.data == 30
    assert str(s) == "Top -> 30 -> 20 -> 10"