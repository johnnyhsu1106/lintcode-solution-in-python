class Solution:
    def twoSumClosest(self, nums, target):
        if not nums or len(nums) == 0:
            return -1;

        nums.sort()
        left, right = 0, len(nums) - 1
        diff = float('inf')

        while left < right:
            diff = min(diff, abs(target - (nums[right] + nums[left])))
            if nums[left] + nums [right] == target:
                return 0
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1

        return diff


# def main():
#     s = Solution()
#     nums = [-1, 2, 1, -4]
#     target = 4
#     print(s.twoSumClosest(nums, target))
# if __name__ == '__main__':
#     main()
