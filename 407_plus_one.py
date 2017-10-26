'''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.


Example
Given [1,2,3] which represents 123, return [1,2,4].

Given [9,9,9] which represents 999, return [1,0,0,0].
'''
class Solution:
    """
    @param: digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):

        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10
        if carry > 0:
            digits.insert(0, carry)

        return digits



# def main():
#     s = Solution()
#     digits = [1, 2, 3]
#     print(s.plusOne(digits))
#
#     digits = [9, 9, 9]
#     print(s.plusOne(digits))
#
# if __name__ == '__main__':
#     main()
