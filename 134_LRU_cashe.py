'''
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key
if the key exists in the cache, otherwise return -1.

set(key, value) - Set or insert the value
if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.
'''


from collections import defaultdict, deque



class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.hashmap = defaultdict(int)
        self.queue = deque()

    def get(self, key):
        value = self.hashmap.get(key)


        if value:
            return value
        return -1


    def set(self, key, value):
        self.hashmap[key] = value


        if self.count < self.capacity:
            self.queue.append(key)

        else:
            self.queue.popleft()
