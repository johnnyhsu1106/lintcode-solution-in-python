'''
Given an expression s includes numbers,
letters and brackets. Number represents the number of repetitions
inside the brackets(can be a string or another expression)．
Please expand expression to be a string.

Example
s = abc3[a] return abcaaa
s = 3[abc] return abcabcabc
s = 4[ac]dy, return acacacacdy
s = 3[2[ad]3[pf]]xyz, return adadpfpfpfadadpfpfpfadadpfpfpfxyz

Challenge
Can you do it without recursion?
'''
class Solution:
    """
    @param: s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        stack = []
        num = ''

        for char in s:
            if char.isdigit():
                num += char

            elif char == '[':
                stack.append(int(num))
                num = ''

            elif char == ']':
                strings = []

                while stack:
                    top = stack.pop()

                    if type(top) == int:
                        stack.append(''.join(reversed(strings)) * top)
                        break
                    else:
                        strings.append(top)
            else:
                stack.append(char)

        return ''.join(stack)



# def main():
#     s = Solution()
#     string = 'abc3[a]'
#     print(s.expressionExpand(string) == 'abcaaa')
#
#     string = '3[abc]'
#     print(s.expressionExpand(string) == 'abcabcabc')
#
#     string = '4[ac]dy'
#     print(s.expressionExpand(string) == 'acacacacdy')
#
#     string = '3[2[ad]3[pf]]xyz'
#     print(s.expressionExpand(string) == 'adadpfpfpfadadpfpfpfadadpfpfpfxyz')
#
#
# if __name__ == '__main__':
#     main()
