'''
Given a collection of intervals, merge all overlapping intervals.

Example
Given intervals => merged intervals:

[                     [
  [1, 3],               [1, 6],
  [2, 6],      =>       [8, 10],
  [8, 10],              [15, 18]
  [15, 18]            ]
]
Challenge
O(n log n) time and O(1) extra space.
'''


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return '[' + str(self.start) + ',' + str(self.end) + ']'


class Solution:
    """
    @param: intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals, key = lambda interval: (interval.start, interval.end))

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if result[-1].end < interval.start:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)

        return result


# def main():
#     s = Solution()
#     intervals = [Interval(8 ,10), Interval(2, 6), Interval(15 ,18), Interval(1, 3)]
#     print(s.merge(intervals))
#
#
# if __name__ == '__main__':
#     main()
