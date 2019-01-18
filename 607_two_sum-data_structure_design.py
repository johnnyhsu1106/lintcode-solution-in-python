'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example
add(1); add(3); add(5);
find(4) // return true
find(7) // return false
'''
from collections import defaultdict
class TwoSum_1:

    def __init__(self):
        self.counts = defaultdict(int)

    """
    Add the number to an internal data structure.
    @param: number: An integer
    @return: nothing
    """
    def add(self, number):
        self.counts[number] += 1

    """
    @param: value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        for num in self.counts:
            remain = value - num
            if remain in self.counts:
                if remain == num and self.counts[num] >= 2:
                    return True
                elif remain != num and self.counts[num] >= 1 and self.counts[remain] >= 1:
                    return True

        return False


class TwoSum_2:
    '''
    this method can not pass the lintcode time limit....
    '''
    def __init__(self):
        self.nums = []


    def add(self, number):
        self.nums.append(number)
        self.nums.sort()


    def find(self, value):
        left, right = 0, len(self.nums) - 1

        while left < right:
            total = self.nums[left] + self.nums[right]
            if total < value:
                left += 1
            elif total > value:
                right -= 1
            else:
                return True

        return False




# def main():
#     two_sum = TwoSum_2()
#     two_sum.add(2)
#     two_sum.add(3)
#     two_sum.add(2)
#     print(two_sum.find(4))
#
#     print(two_sum.find(5))
#
# if __name__ == '__main__':
#     main()
