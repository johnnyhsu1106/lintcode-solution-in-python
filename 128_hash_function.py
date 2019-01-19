class Solution:
    """
    @param: key: A string you should hash
    @param: HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode_1(self, key, HASH_SIZE):
        if not key or len(key) == 0 or HASH_SIZE == 0:
            return -1

        # exceed time limit
        hash_code = 0
        for i in range(len(key)):
            hash_code += ord(key[i]) * 33 ** (len(key) - i - 1)

        return hash_code % HASH_SIZE


    def hashCode_2(self, key, HASH_SIZE):
        if not key or len(key) == 0 or HASH_SIZE == 0:
            return -1

        hash_code = 0

        for char in key:
            hash_code = (hash_code * 33 + ord(char)) % HASH_SIZE

        return hash_code

# def main():
#     s = Solution()
#     key = 'abcd'
#     size = 100
#     print(s.hashCode_1(key, size))
#     print(s.hashCode_2(key, size))
#
# if __name__ == '__main__':
#     main()
