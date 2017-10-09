'''
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key
if the key exists in the cache, otherwise return -1.

set(key, value) - Set or insert the value
if the key is not already present. When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.
'''

###################### Use Doubly List Node###################
# class Node:
#     def __init__(self, key= None, value = None):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None
#
# class LRUCache:
#
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.hash = dict()
#         self.head = Node() # dummy node
#         self.tail = Node() # dummy node
#         self.tail.prev = self.head
#         self.head.next = self.tail
#
#
#     def get(self, key):
#         if key not in self.hash:
#             return - 1
#         # remove current node
#         node = self.hash[key]
#         node.prev.next = node.next
#         node.next.prev = node.prev
#
#         self._move_to_tail(node)
#
#         return self.hash[key].value
#
#
#     def set(self, key, value):
#         if key in self.hash:
#             self.hash[key].value = value # uddate value if value is changed
#             node = self.hash[key]
#         else:
#
#             if len(self.hash) == self.capacity:
#                 del self.hash[self.head.next.key]
#                 self.head.next = self.head.next.next
#                 self.head.next.prev = self.head
#
#             node = Node(key, value)
#             self.hash[key] = node
#
#         self._move_to_tail(node)
#
#
#     def _move_to_tail(self, node):
#         node.prev = self.tail.prev
#         self.tail.prev = node
#         node.prev.next = node
#         node.next = self.tail


###################### Use Singly List Node###################
class Node:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None



# #
# def main():
#     cache = LRUCache(2)
#     cache.set(2, 1)
#     print(cache.hash)
#     cache.set(1, 1)
#     print(cache.hash)
#     # print(cache.get(2))


# if __name__ == '__main__':
#     main()
