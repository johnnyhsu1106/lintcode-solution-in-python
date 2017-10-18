def find_max_diff(nums):
    if nums is None or len(nums) == 0:
        return 0

    max_diff = float('-inf')
    min_val = nums[0]
    for i in range(1, len(nums)):
        max_diff = max(max_diff, nums[i] - min_val)
        min_val = min(min_val, nums[i])
    return max_diff


def main():
    nums = [-10, -4, -7, -9]
    print(find_max_diff(nums))


if __name__ == '__main__':
    main()
