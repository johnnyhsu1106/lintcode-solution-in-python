'''
Given a non-overlapping interval list which is sorted by start point.

Insert a new interval into it,
make sure the list is still in order and non-overlapping (merge intervals if necessary).

Have you met this question in a real interview? Yes
Example
Insert [2, 5] into [[1,2], [5,9]], we get [[1,9]].

Insert [3, 4] into [[1,2], [5,9]], we get [[1,2], [3,4], [5,9]].
'''

# Definition of Interval.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param: intervals: Sorted interval list.
    @param: newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        result = []
        insert_pos = 0

        for interval in intervals:
            if interval.end < newInterval.start:
                result.append(interval)
                insert_pos += 1
            elif interval.start > newInterval.end:
                result.append(interval)
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end = max(interval.end, newInterval.end)

        result.insert(insert_pos, newInterval)

        return result
