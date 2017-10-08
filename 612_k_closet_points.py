'''
Given some points and a point origin in two dimensional space,
find k points out of the some points which are nearest to origin.
Return these points sorted by distance, if they are same with distance,
sorted by x-axis, otherwise sorted by y-axis.

Example
Given points = [[4,6],[4,7],[4,4],[2,5],[1,1]], origin = [0, 0], k = 3
return [[1,1],[2,5],[4,4]]
'''
class Point:
    def __init__(x = 0, y = 0):
        self.x = x
        self.y = y


from collections import defaultdict
class Solution:
    """
    @param: points: a list of points
    @param: origin: a point
    @param: k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):

        result = []
        distances = defaultdict(list)

        for point in points:
            distance_sqrt = abs(point.x - origin.x) ** 2 + abs(point.y - origin.y) ** 2
            distances[distance_sqrt].append((point.x, point.y))
        i = 1
        for distance in sorted(distances.keys()):
            points = distances[distance]
            for x, y in sorted(points):
                result.append(Point(x,y))
                if i == k:
                    return result
                i += 1
