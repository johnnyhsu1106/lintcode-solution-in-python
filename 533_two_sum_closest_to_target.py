class Solution:
    def twoSumClosest(self, nums, target):
        if nums is None or len(nums) == 0:
            return -1;

        nums.sort()
        start, end = 0, len(nums) - 1
        diff = float('inf')

        while start < end:
            diff = min(diff, abs(target - (nums[end] + nums[start])))
            if nums[start] + nums [end] == target:
                return 0
            elif nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1

        return diff


# def main():
#     s = Solution()
#     nums = [-1, 2, 1, -4]
#     target = 4
#     print(s.twoSumClosest(nums, target))
# if __name__ == '__main__':
#     main()
