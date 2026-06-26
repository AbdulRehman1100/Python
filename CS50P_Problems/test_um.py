from um import count
import pytest

def test_between():
    assert count("hello, um, world um no means no but Umhaa") == 2
    assert count("hello, um, world") == 1

def test_edges():
    assert count("Um, pass give me some water") == 1
    assert count("Can you explain um") == 1
    assert count("Um her name should be um") == 2

def test_no_um():
    assert count("") == 0
    assert count("Dear, Abdul Rehman") == 0
