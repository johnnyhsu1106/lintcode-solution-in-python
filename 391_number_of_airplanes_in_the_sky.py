'''
Given an interval list which are flying and landing time of the flight.
How many airplanes are on the sky at most?

Notice

If landing and flying happens at the same time, we consider landing should happen at first.

Example
For interval list

[
  [1,10],
  [2,3],
  [5,8],
  [4,7]
]
Return 3
'''
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def sorter(x, y):
    if x[0] != y[0]:
        return x[0] - y[0]
    return x[1] - y[1]

from functools import cmp_to_key
class Solution:
    """
    @param: airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes_1(self, airplanes):
        times = []
        for airplane in airplanes:
            times.append((airplane.start, 1)) # 1 stands for taking off
            times.append((airplane.end, 0)) #  2 stands for landing

        times.sort()
        count = 0
        max_count = 0
        for time, flag in times:
            if flag == 1:
                count += 1
            else:
                count -= 1
            max_count = max(max_count, count)

        return max_count


    def countOfAirplanes_2(self, airplanes):
        times = []
        for airplane in airplanes:
            times.append((airplane.start, 1))
            times.append((airplane.end, -1))

        times = sorted(times, key = cmp_to_key(sorter))

        count = 0
        max_count = 0
        for time, delta in times:
            count += delta
            max_count = max(max_count, count)

        return max_count


# def main():
#     s= Solution()
#     airplanes = [Interval(1,10),
#                   Interval(2,3),
#                   Interval(5,8),
#                   Interval(4,7)]
#     print(s.countOfAirplanes_2(airplanes))
#     print(s.countOfAirplanes_2(airplanes))
# if __name__ == '__main__':
#     main()
