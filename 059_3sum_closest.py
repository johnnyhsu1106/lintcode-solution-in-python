'''
Given an array S of n integers,
find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers.

Notice

You may assume that each input would have exactly one solution.

Have you met this question in a real interview? Yes
Example
For example, given array S = [-1 2 1 -4], and target = 1. The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Challenge
O(n^2) time, O(1) extra space
'''

class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @param: target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        #please see proble 533 two sum closest (the same idea)
        diff = float('inf')
        numbers.sort()

        for i in range(len(numbers) - 2):
            left, right = i + 1, len(numbers) - 1
            while left < right:
                total = numbers[i] + numbers[left] + numbers[right]
                if abs(total - target) < diff:
                    diff = abs(total - target)
                    closet_sum = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        return closet_sum



# def main():
#     s = Solution()
#     nums = [2, 7, 11, 15]
#     target = 3
#     print(s.threeSumClosest(nums, target))
# if __name__ == '__main__':
#     main()
