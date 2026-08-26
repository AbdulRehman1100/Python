import pytest
from HashTable_OpenAdd import HashTable

def test_insert_and_get():
    ht = HashTable(7)
    ht.insert(100, "Abdul")
    ht.insert(14, "Ali")
    assert ht.get(100) == "Abdul"
    assert ht.get(14) == "Ali"

def test_insert_updates_existing_key():
    ht = HashTable(7)
    ht.insert(100, "Abdul")
    ht.insert(100, "Updated")
    assert ht.get(100) == "Updated"

def test_get_missing_key():
    ht = HashTable(7)
    ht.insert(100, "Abdul")
    assert ht.get(999) is None

def test_remove_existing_key():
    ht = HashTable(7)
    ht.insert(100, "Abdul")
    ht.insert(14, "Ali")
    assert ht.remove(14) == True

def test_remove_missing_key():
    ht = HashTable(7)
    ht.insert(100, "Abdul")
    ht.insert(14, "Ali")
    assert ht.remove(999) == False

def test_remove_then_re_insert_same_key():
    ht = HashTable(7)
    ht.insert(100, "Abdul")
    ht.insert(14, "Ali")
    ht.remove(100)
    ht.insert(100, "Abdul")
    assert ht.get(100) == "Abdul"
    assert ht.get(14) == "Ali"

def test_collision_handling():
    ht = HashTable(7)
    ht.insert(100, "Abdul")
    ht.insert(14, "Ali")
    ht.insert(28, "Saif")
    assert ht.get(14) == "Ali"
    assert ht.get(28) == "Saif"

def test_resize_trigger():
    ht = HashTable(7)
    for i in range(10):
        ht.insert("abc"+str(i), i)

    for i in range(10):
            assert ht.get("abc"+str(i)) == i