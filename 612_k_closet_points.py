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
class Solution:
    """
    @param: points: a list of points
    @param: origin: a point
    @param: k: An integer
    @return: the k closest points
    """
    def kClosest_hash(self, points, origin, k):
        from collections import defaultdict

        # use hash map (dictionary) to store the {dictance : (x, y)}

        result = []
        distances = defaultdict(list)

        for point in points:
            dist = self.get_distance(point, origin)
            distances[dist].append((point.x, point.y))

        i = 1
        for distance in sorted(distances.keys()):
            points = distances[distance]
            for x, y in sorted(points):
                result.append(Point(x,y))
                if i == k:
                    return result
                i += 1


    def get_distance(self, point, origin):
        return abs(point.x - origin.x) ** 2 + abs(point.y - origin.y) ** 2


    def kClosest_heap(self, points, origin, k):
        # In order to use max_heap to solve this problem
        # In python, there is no max heap, so we can use min heap like max heap
        # before push element, reverse the sign
        # after pop elemnt, reverse sign

        max_heap = []
        result = []
        for point in points:
            dist = self.get_distance(point, origin)
            if len(max_heap) < k:
                heappush(max_heap, [-dist, point.x, point.y])
            else:
                if dist < -max_heap[0][0]:
                    heappop(max_heap)
                    heappush(max_heap, [-dist, point.x, point.y])
                elif dist == -max_heap[0][0]:
                    if point.x < max_heap[0][1]:
                        heappop(max_heap)
                        heappush(max_heap, [-dist, point.x, point.y])
                    elif point.x == max_heap[0][1]:
                        if point.y < max_heap[0][2]:
                            heappop(max_heap)
                            heappush(max_heap, [-dist, point.x, point.y])


            # heappush(max_heap, [-dist, point.x, point.y])
            # if len(max_heap) > k:
            #     heappop(max_heap)

        ###################################################################
        # Notice: It might goes wrong if we use the following code.
        # However, among all LintCode test case, it can still pass all tests cases.

        # Assume Point(x1, y1) and oint(x2, y2) is same distance far from origin.
        # x1 < x1 or x1 == x1 and y1 < y2, so they are both kth point
        # We should keep Point(x1, y1) instead of Point(x2, y2)
        # However, the following method might keep Point(x2, y2) instead of Point(x1, y1)
        # Unless, you create the class Type, include dist and point
        # In python 3, __cmp__() is removed. You have to implemnt __ne__(), __lt__() yourself

        ####################################################################


        for i in range(k):
            max_heap[i][0] = - max_heap[i][0]

        for dist, x, y in sorted(max_heap):
            result.append(Point(x,y))

        return result



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
