'''
Given an array of integers, find two numbers that their difference equals to a target value.
where index1 must be less than index2. Please note that your returned answers
(both index1 and index2) are NOT zero-based.

Notice

It's guaranteed there is only one available solution

Example
Given nums = [2, 7, 15, 24], target = 5
return [1, 2] (7 - 2 = 5)
'''
class Solution:
    """
    @param: nums: an array of Integer
    @param: target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        hashmap = dict()
        for i, num in enumerate(nums):
            if num + target not in hashmap and num - target not in hashmap:
                hashmap[num] = i
            else:
                if num + target in hashmap:
                    return [hashmap[num + target] + 1, i + 1]
                else:
                    return [hashmap[num - target] + 1, i + 1]



# def main():
#     s = Solution()
#     nums = [2, 7, 15, 24]
#     target = 5
#     print(s.twoSum7(nums, target))
#
#     nums = [2, 7, 15, 24]
#     target = -5
#     print(s.twoSum7(nums, target))

# if __name__ == '__main__':
#     main()
