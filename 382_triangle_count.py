'''
Given an array of integers,
how many three numbers can be found in the array,
so that we can build an triangle whose three edges length is the three numbers that we find?

Example
Given array S = [3,4,6,7], return 3. They are:

[3,4,6]
[3,6,7]
[4,6,7]
Given array S = [4,4,4,4], return 4. They are:

[4(1),4(2),4(3)]
[4(1),4(2),4(4)]
[4(1),4(3),4(4)]
[4(2),4(3),4(4)]
'''
class Solution:
    """
    @param: S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        S.sort()
        count = 0
        for i in range(2, len(S)):
            left = 0
            right = i - 1
            target = S[i]
            count += self.two_sum(self, S, left, right, target)

        return count


    def two_sum(self, S, left, right, target):
        '''
        please see all two sum problem related
        Remember
        left pointer can go right direction only (left += 1)
        right pointer can go left direction only (right -= 1)


        '''
        count = 0
        while left < right:
            if S[left] +  S[right] <= target:
                left += 1
            else:
                count += (right - left) # for example, [1, 2, 3 ,4], target = 4 , left = 1, right = 4
                right -= 1

        return count


    def triangleCount_2(self, S):
        count = 0
        if not S or len(S) == 0:
            return count

        S.sort()

        for i in range(2, len(S)):
            left, right = 0, i  - 1

            while left < right:
                if S[left] + S[right] > S[i]:
                    count += right - left
                    right -= 1
                elif S[left] + S[right] <= S[i]:
                    left += 1
        return count



# def main():
#     s = Solution()
#     S = [3, 4, 6, 7]
#     #  3
#     print(s.triangleCount_2(S))
#     #  4
#     S = [4, 4, 4, 4]
#     print(s.triangleCount_2(S))
#
# if __name__ == '__main__':
#     main()
