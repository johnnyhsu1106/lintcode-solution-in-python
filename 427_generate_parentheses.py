'''
Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.

Example
Given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
'''
class Solution:
    """
    @param: n: n pairs
    @return: All combinations of well-formed parentheses
    """
    def generateParenthesis(self, n):
        if n == 0:
            return []

        result = []
        paren = ''
        self.helper(n, n, paren, result)

        return result

    def helper(self, left, right, paren, result):
        if left == 0 and right == 0:
            result.append(paren)
            return

        if left > 0:
            self.helper(left - 1, right, paren + '(', result)

        if right > 0 and left < right:
            self.helper(left, right - 1, paren + ')', result)


# def main():
#     s = Solution()
#     n = 3
#     print(s.generateParenthesis(n))
#
# if __name__ == '__main__':
#     main()
