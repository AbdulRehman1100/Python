from LinkedList_based_Queue import Queue
import pytest

def test_enqueue():
    # empty queue
    q = Queue()
    q.enqueue(10)
    assert q._head.data == 10
    assert q._head == q._tail
    assert q._head.next is None
    assert str(q) == "Head -> 10 -> Tail"

    # non empty queue
    q.enqueue(20)
    assert q._head.data == 10
    assert q._head.next == q._tail
    assert q._tail.data == 20
    assert q._tail.next is None
    assert str(q) == "Head -> 10 -> 20 -> Tail"

    # enquque after dequeue
    q.dequeue()
    q.enqueue(30)
    assert q._head.data == 20
    assert q._head.next == q._tail
    assert q._tail.data == 30
    assert q._tail.next is None
    assert str(q) == "Head -> 20 -> 30 -> Tail"

    # enqueue used empty queue
    q.dequeue()
    q.dequeue()
    q.enqueue(99)
    assert q._head.data == 99
    assert q._head == q._tail
    assert q._head.next is None
    assert str(q) == "Head -> 99 -> Tail"

def test_dequeue():
    # empty queue
    q = Queue()
    with pytest.raises(AttributeError):
        q.dequeue()

    # dequeue from queue containing single element
    q.enqueue(10)
    assert q.dequeue() == 10
    assert q._head is None
    assert q._tail is not None  # tail will be stale
    assert str(q) == ""

    # dequeue from queue containing multiple elements
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    assert q.dequeue() == 10
    assert q._head.data == 20
    assert q._tail.data == 30
    assert str(q) == "Head -> 20 -> 30 -> Tail"

def test_is_empty():
      # empty queue
    q = Queue()
    assert q.is_empty() == True
    assert str(q) == ""

    # is_empty after enqueue
    q.enqueue(10)
    assert q.is_empty() == False
    assert str(q) == "Head -> 10 -> Tail"
    q.enqueue(20)
    assert q.is_empty() == False
    assert str(q) == "Head -> 10 -> 20 -> Tail"

    # is_empty after dequeue
    q.dequeue()
    assert q.is_empty() == False
    assert str(q) == "Head -> 20 -> Tail"
    q.dequeue()
    assert q.is_empty() == True
    assert str(q) == ""

def test_front():
    # test empty queue
    q = Queue()
    with pytest.raises(AttributeError):
        q.front()

    # queue containing single element
    q.enqueue(10)
    assert q.front() == 10
    assert q._head.data == 10
    assert str(q) == "Head -> 10 -> Tail"

    # queue containing multiple elements
    q.enqueue(20)
    q.enqueue(30)
    assert q.front() == 10
    assert q._head.data == 10
    assert str(q) == "Head -> 10 -> 20 -> 30 -> Tail"