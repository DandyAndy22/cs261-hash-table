# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Andras Mihaly


class HashTable:

    pass

    def __init__(self, size=10):
        self.size = size
        self.data = [[] for i in range(self.size)]
        self.keys = []

    def __setitem__(self, key, value):
        key_value = [key, value]
        hash_key = self.hash(key)

        self.data[hash_key].append(key_value)

        self.keys.append(key)
    
    def __getitem__(self, key):
        hash_key = self.hash(key)
        key_value = self.data[hash_key]

        for item in key_value:
            if item[0] == key:
                return item[1]


    def hash(self, key):
        key = hash(key)
        key = key % self.size
        return key

    
