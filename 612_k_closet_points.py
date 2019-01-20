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
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return '[' + str(self.x) + ', '  + str(self.y) + ']'

# class Type:
#     def __init__(self, dist, point):
#         self.dist = dist
#         self.point = point
#
#     def __eq__(self, other):
#         return self.dist, self.point.x, self.point.y == other.dist, other.point.x, other.point.y
#
#     def __ne__(self, other):
#         return self.dist != self.dist or self.point.x != other.point.x or self.other.y != other.point.y
#
#     def __gt__(self, other):
#         if self.dist < other.dist:
#             return self.dist < other.dist
#         if self.point.x < other.point.x:
#             return self.point.x < other.point.x
#         if self.point.y < other.point.y:
#             return self.point.y < other.point.y
#
#     def __lt__(self, other):
#         if self.dist > other.dist:
#             return self.dist > other.dist
#         if self.point.x > other.point.x:
#             return self.point.x > other.point.x
#         if self.point.y > other.point.y:
#             return self.point.y > other.point.y
#
#     def __repr__(self):
#         return str(self.dist) + ',' + str(self.point)

from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    """
    @param: points: a list of points
    @param: origin: a point
    @param: k: An integer
    @return: the k closest points
    """
    def kClosest_hash(self, points, origin, k):
        if not points or not origin or k == 0:
            return

        # use hash map (dictionary) to store the {dictance : (x, y)}

        k_closest_points = []
        distance_mapping = defaultdict(list)

        for point in points:
            dist = self._get_distance(point, origin)
            distance_mapping[dist].append((point.x, point.y))

        count = 0
        for distance in sorted(distance_mapping.keys()):
            points = distance_mapping[distance]

            for x, y in sorted(points):
                k_closest_points.append(Point(x, y))
                count += 1

                if count == k:
                    return k_closest_points


    def _get_distance(self, point, origin):
        return abs(point.x - origin.x) ** 2 + abs(point.y - origin.y) ** 2




    def kClosest_heap(self, points, origin, k):
        # In order to use max_heap to solve this problem
        # In python, there is no max heap, so we can use min heap like max heap
        # before push element, reverse the sign
        # after pop elemnt, reverse sign

        if not points or not origin or k == 0:
            return
        # get top k closest points in max_heap
        max_heap = []

        for point in points:
            distance = self._get_distance(point, origin)
            heappush(max_heap, (-distance, -point.x, -point.y))

            if len(max_heap) > k:
                heappop(max_heap)


        k_closest_points = []
        # get top k closest points from max heap in descending order
        while max_heap > 0:
            distance, x, y = heappop(max_heap)
            k_closest_points.append(Point(-x, -y))
        # get top k closest points in ascending order as problem requested.
        k_closest_points.reverse();

        return k_closest_points


    def _get_distance(self, point, origin):
        return abs(point.x - origin.x) ** 2 + abs(point.y - origin.y) ** 2

# def main():
#     s = Solution()
#     points = [Point(4, 6), Point(4, 7), Point(4, 4), Point(2, 5), Point(1, 1)]
#     origin = Point(0,0)
#     k = 3
#     print(s.kClosest_hash(points, origin, k))
#     print(s.kClosest_heap(points, origin, k))
#
#     points = [Point(-1, -1), Point(1, 1), Point(100, 100)]
#     origin = Point(0,0)
#     k = 2
#     print(s.kClosest_hash(points, origin, k))
#     print(s.kClosest_heap(points, origin, k))
#
#
# if __name__ == '__main__':
#     main()
