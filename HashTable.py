
# The class that holds the methods for the Hash Table
class HashTable:

# constructor for the Hash Table
    def __init__(self, initial_capacity=10):

        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

# insert method for Hash Table
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        key_value = [key, item]
        bucket_list.append(key_value)
        return True

# search method for the Hash Table
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None
