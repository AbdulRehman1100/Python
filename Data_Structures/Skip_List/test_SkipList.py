from SkipList import SkipList

def test_random_level():
    sk = SkipList(-9999, 9999, 5)

    for i in range(100):
        level = sk._random_level()
        assert 0 <= level <= sk._max_level

def test_insert_empty():
    sk = SkipList(-9999, 9999, 5)

    # insert empty SkipList
    sk.insert(100)
    assert sk.get_level_0_items() == [100]

def test_insert_at_begining():
    sk = SkipList(-9999, 9999, 5)
    sk.insert(100)
    sk.insert(200)
    sk.insert(500)
    sk.insert(400)
    sk.insert(800)
    sk.insert(700)
    sk.insert(300)
    sk.insert(900)
    sk.insert(600)

    # insert at begining
    sk.insert(99)
    assert sk.get_level_0_items() == [99, 100, 200, 300, 400, 500, 600, 700, 800, 900]

def test_insert_at_end():
    sk = SkipList(-9999, 9999, 5)
    sk.insert(100)
    sk.insert(200)
    sk.insert(500)
    sk.insert(400)
    sk.insert(800)
    sk.insert(700)
    sk.insert(300)
    sk.insert(900)
    sk.insert(600)

    # insert at end
    sk.insert(999)
    assert sk.get_level_0_items() == [100, 200, 300, 400, 500, 600, 700, 800, 900, 999]

def test_insert_at_middle():
    sk = SkipList(-9999, 9999, 5)
    sk.insert(100)
    sk.insert(200)
    sk.insert(500)
    sk.insert(400)
    sk.insert(800)
    sk.insert(700)
    sk.insert(300)
    sk.insert(900)
    sk.insert(600)

    # insert at middle
    sk.insert(499)
    assert sk.get_level_0_items() == [100, 200, 300, 400, 499, 500, 600, 700, 800, 900]

def test_insert_many_values():
    sk = SkipList(-9999, 9999, 5)
    values = [40, 10, 80, 20, 70, 30, 60, 50]
    for value in values:
        sk.insert(value)
    assert sk.get_level_0_items() == sorted(values)

def test_insert_duplicates():
    sk = SkipList(-9999, 9999, 5)
    sk.insert(300)
    sk.insert(500)
    sk.insert(400)
    sk.insert(100)
    sk.insert(100)
    sk.insert(700)
    sk.insert(200)
    sk.insert(600)
    sk.insert(600)

    assert sk.get_level_0_items() == [100, 100, 200, 300, 400, 500, 600, 600, 700]

def test_insert_after_remove():
    sk = SkipList(-9999, 9999, 5)
    sk.insert(100)
    sk.insert(200)
    sk.insert(500)
    sk.insert(400)
    sk.insert(800)
    sk.insert(700)
    sk.insert(300)
    sk.insert(900)
    sk.insert(600)

    sk.remove(400)
    sk.insert(399)
    sk.insert(401)
    assert sk.get_level_0_items() ==  [100, 200, 300, 399, 401, 500, 600, 700, 800, 900]
    sk.insert(400)
    assert sk.get_level_0_items() ==  [100, 200, 300, 399, 400, 401, 500, 600, 700, 800, 900]

def test_search_empty():
    sk = SkipList(-9999, 9999, 5)
    assert sk.search(99) is None

def test_search_success():
    sk = SkipList(-9999, 9999, 5)
    sk.insert(100)
    sk.insert(200)
    sk.insert(500)
    sk.insert(400)
    sk.insert(800)
    sk.insert(700)
    sk.insert(300)
    sk.insert(900)
    sk.insert(600)

    assert sk.search(100).data == 100
    assert sk.search(500).data == 500
    assert sk.search(900).data == 900

def test_search_failure():
    sk = SkipList(-9999, 9999, 5)
    sk.insert(100)
    sk.insert(200)
    sk.insert(500)
    sk.insert(400)
    sk.insert(800)
    sk.insert(700)
    sk.insert(300)
    sk.insert(900)
    sk.insert(600)

    assert sk.search(99) is None
    assert sk.search(450) is None
    assert sk.search(1000) is None
    assert sk.search(399) is None
    assert sk.search(401) is None

def test_remove_empty():
    sk = SkipList(-9999, 9999, 5)

    # remove
    assert sk.remove(200) == False

def test_remove_at_begining():
    sk = SkipList(-9999, 9999, 5)
    sk.insert(100)
    sk.insert(200)
    sk.insert(500)
    sk.insert(400)
    sk.insert(800)
    sk.insert(700)
    sk.insert(300)
    sk.insert(900)
    sk.insert(600)

    assert sk.remove(100) == True
    assert sk.get_level_0_items() == [200, 300, 400, 500, 600, 700, 800, 900]

def test_remove_at_end():
    sk = SkipList(-9999, 9999, 5)
    sk.insert(100)
    sk.insert(200)
    sk.insert(500)
    sk.insert(400)
    sk.insert(800)
    sk.insert(700)
    sk.insert(300)
    sk.insert(900)
    sk.insert(600)

    assert sk.remove(900) == True
    assert sk.get_level_0_items() == [100, 200, 300, 400, 500, 600, 700, 800]

def test_remove_at_middle():
    sk = SkipList(-9999, 9999, 5)
    sk.insert(100)
    sk.insert(200)
    sk.insert(500)
    sk.insert(400)
    sk.insert(800)
    sk.insert(700)
    sk.insert(300)
    sk.insert(900)
    sk.insert(600)

    assert sk.remove(500) == True
    assert sk.get_level_0_items() == [100, 200, 300, 400, 600, 700, 800, 900]

def test_remove_at_multiple_values():
    sk = SkipList(-9999, 9999, 5)
    sk.insert(100)
    sk.insert(200)
    sk.insert(500)
    sk.insert(400)
    sk.insert(800)
    sk.insert(700)
    sk.insert(300)
    sk.insert(900)
    sk.insert(600)

    assert sk.remove(300) == True
    assert sk.remove(700) == True
    assert sk.get_level_0_items() == [100, 200, 400, 500, 600, 800, 900]

def test_remove_duplicate_values():
    sk = SkipList(-9999, 9999, 5)
    sk.insert(100)
    sk.insert(200)
    sk.insert(500)
    sk.insert(800)
    sk.insert(400)
    sk.insert(800)
    sk.insert(700)
    sk.insert(300)
    sk.insert(900)
    sk.insert(600)

    assert sk.remove(800) == True
    assert sk.remove(800) == True
    assert sk.get_level_0_items() == [100, 200, 300, 400, 500, 600, 700, 900]