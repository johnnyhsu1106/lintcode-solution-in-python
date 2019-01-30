class Solution:
    def twoSumClosest(self, nums, target):
        if not nums:
            return target;

        nums.sort()
        left, right = 0, len(nums) - 1
        diff = float('inf')

        while left < right:
            total = nums[left] + nums[right]

            if total < target:
                min_diff = min(min_diff, target - total)
                left += 1
            elif total > target:
                min_diff = min(min_diff, total - target)
                right -= 1
            else:
                return 0

        return min_diff


# def main():
#     s = Solution()
#     nums = [-1, 2, 1, -4]
#     target = 4
#     print(s.twoSumClosest(nums, target))
# if __name__ == '__main__':
#     main()
