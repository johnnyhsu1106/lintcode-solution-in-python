'''
There are a total of n courses you have to take, labeled from 0 to n - 1.
Some courses may have prerequisites,
for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs,
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all courses, return an empty array.

Have you met this question in a real interview? Yes
Example
Given n = 2, prerequisites = [[1,0]]
Return [0,1]

Given n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Return [0,1,2,3] or [0,2,1,3]

'''
from collections import defaultdict, deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):

        # convert prerequisites to course map = {couse: []}
        # Calculate the indegree for each course

        course_map = defaultdict(list)
        indegree = defaultdict(int)
        #  Initialize the indegree
        for course in range(numCourses):
            indegree[course] = 0

        for course, pre_course in prerequisites:
            indegree[course] += 1
            course_map[pre_course].append(course)

        # Get the course with indegree 0
        pre_courses = []
        for course in range(numCourses):
            if indegree[course] == 0:
                pre_courses.append(course)

        # Use BFS to sort the couses by indegree accend ascending
        course_order = []
        queue = deque(pre_courses)
        while queue:
            course = queue.popleft()
            course_order.append(course)
            for next_course in course_map[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        if numCourses != len(course_order):
            return []
        return course_order


# def main():
#     s = Solution()
#     #
#     numCourses = 2
#     prerequisites = [[1,0]]
#     print(s.findOrder(numCourses, prerequisites))
#     numCourses = 4
#     prerequisites = [[1,0],[2,0],[3,1],[3,2]]
#     print(s.findOrder(numCourses, prerequisites))
#
#     numCourses = 10
#     prerequisites = [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]
#     print(s.findOrder(numCourses, prerequisites))
#
# if __name__ == '__main__':
#     main()
