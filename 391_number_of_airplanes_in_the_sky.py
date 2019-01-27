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

class Solution:
    """
    @param: airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes_1(self, airplanes):
        schedule = []

        for airplane in airplanes:
            # (time, is_flying)
            schedule.append((airplane.start, True)) # True stands for taking off
            schedule.append((airplane.end, False)) # False stands for landing

        schedule.sort()

        count = 0
        max_count = 0

        for time, is_flying in schedule:
            if is_flying:
                count += 1
            else:
                count -= 1
            max_count = max(max_count, count)

        return max_count


    def countOfAirplanes_2(self, airplanes):
        schedule = []

        for airplane in airplanes:
            schedule.append((airplane.start, 1))
            schedule.append((airplane.end, -1))

        schedule.sort()
        
        count = 0
        max_count = 0

        for time, delta in schedule:
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
