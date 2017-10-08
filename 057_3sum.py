'''
Given an array S of n integers, are there elements a, b, c in S
such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.

For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:

(-1, 0, 1)
(-1, -1, 2)
'''
class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum_1(self, numbers):
        result = []
        if not numbers or len(numbers) < 3:
            return result

        numbers.sort()

        for i in range(len(numbers) - 2):
            if i == 0 or numbers[i] != numbers[i - 1]:
                self.two_sum(numbers, i + 1 , len(numbers) - 1, numbers[i] * -1, result)

        return result


    def two_sum(self, nums, left, right, target, result):

        while left < right:

            if nums[left] + nums[right] < target:
                left += 1

            elif nums[left] + nums[right] > target:
                right -= 1

            else:
                triple = [-target, nums[left], nums[right]]
                result.append(triple)
                left += 1
                right -= 1
                #  avoind all duplicate number, which is equal to nums[left - 1](the previous one)
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                #  avoind all duplicate number, which is equal to nums[right + 1](the previous one)
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    def threeSum_2(self, numbers):

        if not numbers or len(numbers) < 3:
            return []

        result = []
        numbers.sort()
        for i in range(0, len(numbers) - 2):
            if i == 0 or numbers[i] != numbers[i - 1]:
                left, right = i + 1, len(numbers) - 1

                while left < right:
                    total = numbers[left] + numbers[right] + numbers[i]

                    if total == 0:
                        tripple = [numbers[i], numbers[left], numbers[right]]
                        result.append(tripple)
                        left += 1
                        right -= 1

                        while left < right and numbers[left] == numbers[left - 1]:
                            left += 1
                        while left < right and numbers[right] == numbers[right + 1]:
                            right -= 1

                    elif total > 0:
                        right  -= 1
                    else:
                        left += 1

        return result


# 
# def main():
#     s = Solution()
#     nums = [-1, 0, 1, 2, -1, -4]
#     print(s.threeSum_1(nums))
#     print(s.threeSum_2(nums))
#
#
# if __name__ == '__main__':
#     main()
