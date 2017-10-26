# '''
# Write a function, give a string A consisting of N characters
# and a string B consisting of M characters,
# returns the number of times A must be stated
# such that B is a substring of the repeated string.
# If B can never be a substring of the repeated A, then your function should return -1.
#
# Notice
#
# Assume that 1 <= N, M <= 1000
#
# Example
# Given A = abcd, B = cdabcdab
#
# your function should return 3,
# bcause after stating string A three times we otain the string abcdabcdabcd.
# String B is a substring of this string.
# '''
# class Solution:
#     """
#     @param: : string A to be repeated
#     @param: : string B
#     @return: the minimum number of times A has to be repeated
#     """
#
#     def repeatedString(self, A, B):
#
#         if len(A) > len(B):
#             if not set(B).issubset(set(A)):
#                 return -1
#         else:
#             if set(A) != set(B):
#                 return -1
#
#
#         if len(A) <= len(B):
#             if len(B) % len(A) == 0:
#                 min_times = len(B) // len(A)
#             else:
#                 min_times = len(B) // len(A) + 1
#         else:
#             min_times = 1
#
#         while True:
#             A = A * min_times
#             found = A.find(B)
#             if found != -1:
#                 return min_times
#
#             min_times += 1
#
#
#
# def main():
#     s = Solution()
#     A = 'abcd'
#     B = 'cdabcdab'
#     print(s.repeatedString(A, B))
#
#     A = "jcwsijl"
#     B = "sijljcwsijljcwsijljcwsijljcwsijljcwsijljcwsijljcwsijljcwsijljcwsijljc"
#     print(s.repeatedString(A, B))
#
#     A = "wraasr"
#     B= "r"
#     print(s.repeatedString(A, B))
#
#     A = "abcd"
#     B = "abcab"
#     print(s.repeatedString(A, B))
#     # not pass this case
#     # A = 'abcd'
#     # B = 'bdca'
#     #
#     # print(s.repeatedString(A, B))
#
#
# if __name__ == '__main__':
#     main()
