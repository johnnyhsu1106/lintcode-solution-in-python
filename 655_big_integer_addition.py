'''
Given two non-negative integers num1 and num2 represented as string,
return the sum of num1 and num2.

Notice

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
Example
Given num1 = "123", num2 = "45"
return "168"
'''
class Solution:
    """
    @param: num1: a non-negative integers
    @param: num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        if len(num1) == 0 and len(num2) == 0:
            return 0

        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        result = ''

        while i >= 0 or j >= 0:
            if i >= 0:
                carry += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                carry += ord(num2[j]) - ord('0')
                j -= 1

            result = str(carry % 10) + result
            carry = carry // 10

        if carry > 0:
            result = str(carry) + result

        return result


# def main():
#     s = Solution()
#     num1 = '199'
#     num2 = '1'
#     print(s.addStrings(num1, num2))
#
#     num1 = '9999999999981'
#     num2 = '19'
#     print(s.addStrings(num1, num2))

#
# if __name__ == '__main__':
#     main()
