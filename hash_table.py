# HashTable: An unordered key-value data structure providing O(1) store, retrieve
# search and delete operations.
# Your implementation should pass the tests in test_hash_table.py.
# Andras Mihaly


class HashTable:

    pass

    def __init__(self, size=10):
        self.size = size
        self.data = [[] for i in range(self.size)]
        self.keyss = []
        self.valuess = []

    def __setitem__(self, key, value):
        key_value = [key, value]
        hash_key = self.hash(key)

        for  pair in self.data[hash_key]:
            if pair[0] == key:
                pair[1] = value 
                return
        self.data[hash_key].append(key_value)
        self.keyss.append(key)
        self.valuess.append(value)

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

    def delete(self, key):
        hash_key = self.hash(key)
        for  pair in self.data[hash_key]:
            if pair[0] == key:
                pair[1] = None
                return

    def clear(self):
        self.data.clear()
        self.data = [[] for i in range(self.size)]

    def keys(self):
        keys = []
        return self.keyss

    def values(self):
        values = []
        return self.valuess

    

