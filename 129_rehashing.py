'''
The size of the hash table is not determinate at the very beginning.
If the total size of keys is too large (e.g. size >= capacity / 10),
we should double the size of the hash table and rehash every keys.
Say you have a hash table looks like below:

size=3, capacity=4

[null, 21, 14, null]
       ↓    ↓
       9   null
       ↓
      null
The hash function is:

int hashcode(int key, int capacity) {
    return key  %  capacity;
}
here we have three numbers, 9, 14 and 21,
where 21 and 9 share the same position
as they all have the same hashcode 1 (21 % 4 = 9 % 4 = 1).
We store them in the hash table by linked list.

rehashing this hash table, double the capacity, you will get:

size=3, capacity=8

index:   0    1    2    3     4    5    6   7
hash : [null, 9, null, null, null, 21, 14, null]
Given the original hash table, return the new hash table after rehashing .

Notice

For negative integer in hash table, the position can be calculated as follow:

C++/Java: if you directly calculate -4 % 3 you will get -1.
You can use function: a % b = (a % b + b) % b to make it is a non negative integer.
Python: you can directly use -1 % 3, you will get 2 automatically.

Example
Given [null, 21->9->null, 14->null, null],

return [null, 9->null, null, null, null, 21->null, 14->null, null]
'''

class ListNode():

    def __init__(self, val):
        self.val = val
        self.next = None


    def __repr__(self):
        return str(self.val)


class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        if not hashTable or len(hashTable) == 0:
            return hashTable

        capacity = len(hashTable)
        new_capacity = 2 * capacity
        new_hashTable = [None for i in range(new_capacity)]

        for node in hashTable:

            while node:
                hashcode = node.val % new_capacity

                if new_hashTable[hashcode] is None:
                    new_hashTable[hashcode] = ListNode(node.val)
                else:
                    head = new_hashTable[hashcode]
                    while head.next:
                        head = head.next
                    head.next = ListNode(node.val)

                node = node.next

        return new_hashTable


# def main():
#     s = Solution()
#     capacity = 4
#     hashTable = [None] * capacity
#
#     hashTable[1] = ListNode(21)
#     hashTable[1].next = ListNode(9)
#     hashTable[2] = ListNode(14)
#
#     new_hashTable = s.rehashing(hashTable)
#     print(new_hashTable)
#
#
# if __name__ == '__main__':
#     main()
