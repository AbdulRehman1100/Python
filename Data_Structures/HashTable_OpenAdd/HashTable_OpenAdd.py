from functions import is_prime, next_prime

class DeleteMarker:
    pass
DELETED = DeleteMarker()


class HashTable:
    KEY_INDEX = 0
    VALUE_INDEX = 1
    LOAD_FACTOR_THRESHOLD = 0.7
    
    def __init__(self, capacity):
        if type(capacity) != int:
            raise TypeError("Table capacity must be an integer")
        if capacity < 1:
            raise ValueError("Table capacity can't be non positive") 
               
        self._table_capacity = capacity if is_prime(capacity) else next_prime(capacity)
        self._table = [None] * self._table_capacity
        self.table_size = 0

    def _resize(self):
        old_table = [x for x in self._table if x is not DELETED and x is not None]
        self._table_capacity = next_prime(self._table_capacity * 2)
        self._table = [None] * self._table_capacity

        for key, value in old_table:
            self.insert(key, value)

    def insert(self, key, value):
        if key is None:
            raise TypeError("Key can't be None")
        
        # resize before the table becomes too crowded
        if ((self.table_size + 1) / self._table_capacity) > HashTable.LOAD_FACTOR_THRESHOLD:
            self._resize()

        index = hash(key) % self._table_capacity
        probes = 0

        while probes < self._table_capacity:
            if self._table[index] is None:
                self._table[index] = (key, value) # storing key, value pair as tuple
                self.table_size += 1
                return
            #update existing key
            if self._table[index] is not DELETED and self._table[index][HashTable.KEY_INDEX] == key:
                self._table[index] = (key, value)
                return 
            
            index = (index + 1) % self._table_capacity
            probes += 1


    def get(self, key):
        if key is None:
            raise TypeError("Key can't be None")
        
        index = hash(key) % self._table_capacity
        probes = 0
        
        while probes < self._table_capacity:
            if self._table[index] is None:
                return None  # slot khaali, key exist nahi karti
            if self._table[index] is not DELETED and self._table[index][HashTable.KEY_INDEX] == key:
                return self._table[index][HashTable.VALUE_INDEX]
            
            index = (index + 1) % self._table_capacity
            probes += 1
        
        return None  # poora table check ho gaya, nahi mili

    def remove(self, key):
        if key is None:
            raise TypeError("Key can't be None")
        
        index = hash(key) % self._table_capacity
        probes = 0

        while probes < self._table_capacity:
            if self._table[index] is None:
                return False
            
            if self._table[index] is not DELETED and self._table[index][HashTable.KEY_INDEX] == key:
                self._table[index] = DELETED
                return True

            index = (index + 1) % self._table_capacity
            probes += 1

        return False

ht = HashTable(7)
for i in range(10):
    ht.insert(i, "emp"+str(i))

for i in range(10):
    print(ht.get(i), i)