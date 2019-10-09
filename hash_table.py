# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Andras Mihaly


class HashTable:

    pass

    def __init__(self, size=10):
        self.size = size
        self.data = []
        self.keys = []

    def __setitem__(self, key, value):
        #OR .append(value)
        self.data = value
        self.keys = key
    
    def __getitem__(self, key):
        for k in self.keys:
            if k == key:
                return self.data[k]