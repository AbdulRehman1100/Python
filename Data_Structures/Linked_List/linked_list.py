
class Node:
    def __init__(self, data = None):
        self._data = data
        self._next = None

    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, next):
        self._next = next

class LinkedList:
    """
    Cursor-based singly linked list with a dummy head node.

    Unlike standard append-only lists, add_after_current() inserts
    after the current cursor position, not always at the end.
    Use start()/move_next() to navigate the cursor before inserting
    or removing at a specific position.
    """
    def __init__(self):
        self.head = Node()
        self.head.next = None
        self.current = None
        self.last_current = None
        self.size = 0
    
    def add_after_current(self, value = None):
        """
        Inserts a new node containing value immediately after the
        current cursor position. If the list is empty, the new node
        becomes the first node and cursor will point to new node.

        Special case: if current is None on a non-empty list (cursor
        was invalidated by a prior removal), this will raise an error—
        call start() first to reposition the cursor.
        """
        new_node = Node(value)

        if self.head.next == None:
            self.head.next = new_node
            self.current = new_node
            self.last_current = self.head
        elif self.current is None:
            raise ValueError("Cursor is not positioned. Call start() first.")
        else:
            new_node.next = self.current.next
            self.current.next = new_node
            self.last_current = self.current
            self.current = new_node

        self.size += 1
    
    def __str__(self):
        elements = []
        current = self.head.next
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)
    
    def move_next(self):
        """
        Advances current to the next node.

        Returns True if the move succeeded (current now points to a
        valid node). Returns False if current was already None, or if
        current is at the last node — in the latter case, current is
        left unchanged (still points to the last node).
        """
        if self.current is not None and self.current.next is not None:
            self.last_current = self.current
            self.current = self.current.next
            return True
        return False
    
    def find(self, value):
        """
        Searches the list for a node containing value, without moving
        the cursor (current/last_current are untouched).

        Returns the matching Node if found, None otherwise.
        """
        current = self.head.next
        while current is not None:
            if value == current.data:
                return current
            current = current.next
        return None
    
    def start(self):
        """
        Resets the cursor to the first node in the list (or None if
        the list is empty). This is the only way to recover a valid
        cursor position after it has been invalidated by a removal.
        """
        self.current = self.head.next
        self.last_current = self.head

    def remove_current(self):
        """
        Removes the node at the current cursor position.

        After removal, current moves to the next node. If the removed
        node was the last node in the list, current becomes None.

        Returns True if a node was removed, False if current was
        already None (empty list or cursor already invalidated).
        """
        if self.current is not None:
            self.last_current.next = self.current.next
            self.current = self.last_current.next
            self.size -= 1
            return True
        
        return False

    def __len__(self):
        return self.size
    
    def is_empty(self):
        if len(self) == 0:
            return True
        return False
    
    def insert_at(self, value, position):
        """
        Inserts a new node containing value at the given position
        (0-indexed; position 0 means "insert at the very front").
        Valid positions range from 0 to len(self) inclusive.

        Special case: this method temporarily moves current/last_current
        to traverse to the target position, then restores them to their
        original values afterward — so calling insert_at() does not
        change where the cursor was pointing, UNLESS the list was empty
        before the call, in which case current now points to the newly
        inserted (first) node.

        Raises IndexError if position is negative or greater than the
        current list size.
        """
        if position < 0 or position > self.size:
            raise IndexError
        
        is_empty = self.is_empty()
        saved_current = self.current
        saved_last_current = self.last_current
        
        new_node = Node(value)
        
        if self.head.next is None:
            self.head.next = new_node
            self.last_current = self.head
            self.current = new_node
        else:
            self.current = self.head
            i = 0
            while i < position:
                self.last_current = self.current
                self.current = self.current.next
                i += 1
            
            self.last_current = self.current
            new_node.next = self.current.next
            self.current.next = new_node
        
        if not is_empty:
            self.current = saved_current
            self.last_current = saved_last_current
        self.size += 1

    def remove_by_value(self, value):
        """
        Searches the list for the first node containing value and
        removes it.

        Special case: if the removed node was the cursor's current
        position, current becomes None regardless of where the node
        was in the list (start, middle, or end) — this avoids silently
        moving the cursor without the caller explicitly requesting it.
        If the removed node was NOT the current node, current and its
        position are left unchanged.

        Returns True if the value was found and removed, False if the
        value was not in the list (or the list was empty).
        """
        if self.is_empty():
            return False
        
        saved_current = self.current
        saved_last_current = self.last_current
        
        self.current = self.head
        while True:
            if not self.move_next():
                self.current = saved_current
                self.last_current = saved_last_current
                return False
            if self.current.data == value:
                break
        
        was_current = (self.current == saved_current)
        
        self.last_current.next = self.current.next
        self.size -= 1
        
        if was_current:
            self.current = None
            self.last_current = None
        else:
            self.current = saved_current
            self.last_current = saved_last_current
        
        return True
        