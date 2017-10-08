class Solution:
    """
    @param: key: A string you should hash
    @param: HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode_1(self, key, HASH_SIZE):
        # exceed time limit
        hash_code = 0
        for i in range(len(key)):
            hash_code += ord(key[i]) * 33 ** (len(key) - i - 1)
        return hash_code % HASH_SIZE


    def hashCode_2(self, key, HASH_SIZE):
        ans = 0
        for x in key:
            ans = (ans * 33 + ord(x)) % HASH_SIZE
        return ans


# def main():
#     s = Solution()
#     key = 'abcd'
#     size = 100
#     print(s.hashCode_1(key, size))
#     print(s.hashCode_2(key, size))
#
# if __name__ == '__main__':
#     main()
