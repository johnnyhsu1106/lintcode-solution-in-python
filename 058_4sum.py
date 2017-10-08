'''
Given an array S of n integers, are there elements a, b, c, and d in S
such that a + b + c + d = target?

Find all unique quadruplets in the array which gives the sum of target.

Notice

Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.

Example
Given array S = {1 0 -1 0 -2 2}, and target = 0. A solution set is:

(-1, 0, 0, 1)
(-2, -1, 1, 2)
(-2, 0, 0, 2)
'''
class Solution:
    """
    @param: numbers: Give an array
    @param: target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        if not numbers or len(numbers) < 4:
            return []

        result = []
        numbers.sort()

        for i in range(0, len(numbers) - 3):
            if i == 0 or numbers[i] != numbers[i - 1]:
                for j in range(i + 1, len(numbers) -2):
                    if j == i + 1 or numbers[j] != numbers[j - 1]:

                        left, right = j + 1, len(numbers) - 1

                        while left < right:
                            total = numbers[i] + numbers[j] + numbers[left] + numbers[right]
                            if total < target:
                                left += 1
                            elif total > target:
                                right -= 1
                            else:
                                result.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                                left += 1
                                right -= 1

                                while left < right and numbers[left] == numbers[left -1]:
                                    left += 1
                                while left < right and numbers[right] == numbers[right + 1]:
                                    right -= 1


        return result



# def main():
#     s = Solution()
#     numbers = [1,0,-1,-1,-1,-1,0,1,1,1,2]
#     print(sorted(numbers))
#     target = 2
#     # [[-1,0,1,2],[-1,1,1,1],[0,0,1,1]]
#     print(s.fourSum(numbers, target))
#
# if __name__ == '__main__':
#     main()
