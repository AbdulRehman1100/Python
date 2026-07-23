# LinkedList (Cursor-Based)

A singly linked list implementation using a **cursor** (`current`) that
the caller navigates explicitly with `start()` / `move_next()`, rather
than a standard index-based or always-append-at-end design.

This design was learned from a Data Structures course (originally in
C++) and reimplemented in Python. It differs from a typical textbook
linked list in one key way: `add_after_current()` inserts **after
wherever the cursor currently is**, not always at the end of the list.

## Structure

- Uses a **dummy head node** (`self.head`) — it never holds real data,
  it just simplifies edge cases (inserting/removing at the front works
  the same as anywhere else in the list).
- `current` — the cursor; points to the node the next operation will
  act on.
- `last_current` — tracks the node just before `current`, needed for
  removal (since this is a singly linked list, you can't look
  backwards).

## Usage

```python
ll = LinkedList()
ll.add_after_current(1)
ll.add_after_current(2)
ll.add_after_current(3)
print(ll)  # 1 -> 2 -> 3

ll.start()          # cursor -> Node(1)
ll.move_next()      # cursor -> Node(2)
ll.remove_current()  # removes Node(2)
print(ll)  # 1 -> 3

ll.insert_at(99, 1)  # insert 99 at position 1 (0-indexed)
print(ll)  # 1 -> 99 -> 3

ll.remove_by_value(99)
print(ll)  # 1 -> 3
```

## Methods

| Method | Description |
|---|---|
| `add_after_current(value)` | Inserts a new node after the current cursor position. First node if list is empty. |
| `remove_current()` | Removes the node at the current cursor position. Cursor moves to the next node (or `None` if it was the last node). |
| `remove_by_value(value)` | Finds and removes the first node matching `value`. If that node was the cursor's position, cursor becomes `None` regardless of where it was in the list. Returns `True`/`False`. |
| `insert_at(value, position)` | Inserts at a specific 0-indexed position. Cursor position is preserved after the call (unless the list was empty before, in which case it becomes the new node). Raises `IndexError` for invalid positions. |
| `find(value)` | Returns the matching node, or `None`. Does not move the cursor. |
| `start()` | Resets cursor to the first node (or `None` if list is empty). The only way to recover a valid cursor after it's been invalidated. |
| `move_next()` | Advances the cursor. Returns `True`/`False`. Cursor is left unchanged if already at the last node. |
| `__str__` | Returns a readable `"1 -> 2 -> 3"` style string. |
| `__len__` | Returns the number of elements. |
| `is_empty()` | Returns `True`/`False`. |

## Known Design Notes

- Cursor-based `add`/`remove` means operations act on the cursor's
  current position, not a fixed end. Use `start()`/`move_next()` to
  position the cursor before calling them.
- `remove_current()` vs `remove_by_value()` handle a removed cursor
  slightly differently — see their docstrings for the exact rule.
- Tested with `pytest` — see `test_linked_list.py` for coverage of
  empty-list, single-element, front/middle/end, and invalid-input cases.