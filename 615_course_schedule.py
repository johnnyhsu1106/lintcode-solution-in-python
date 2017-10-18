'''
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites,
for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
is it possible for you to finish all courses?

Example
Given n = 2, prerequisites = [[1,0]]
Return true

Given n = 2, prerequisites = [[1,0],[0,1]]
Return false
'''
from collections import defaultdict, deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        indegree = [0] * numCourses
        course_map = defaultdict(list)

        #  get the indegree and course_map = {precourse: [course1, course2...]}
        for course, precourse in prerequisites:
            indegree[course] += 1
            course_map[precourse].append(course)
        # find all precourse, whose indegree is 0
        precourses = []
        for course in range(numCourses):
            if indegree[course] == 0:
                precourses.append(course)

        if len(precourses) == 0:
            return False

        queue = deque(precourses)
        count_courses = 0
        while queue:
            size = len(queue)
            for i in range(size):
                course = queue.popleft()
                count_courses += 1
                for next_course in course_map[course]:
                    indegree[next_course] -= 1
                    if indegree[next_course] == 0:
                        queue.append(next_course)

        return count_courses == numCourses



# def main():
#     s = Solution()
#     numCourses = 2
#     prerequisites = [[1,0]]
#     print(s.canFinish(numCourses, prerequisites))
#
#     numCourses = 2
#     prerequisites = [[1,0], [0,1]]
#     print(s.canFinish(numCourses, prerequisites))
#
#     numCourses = 10
#     prerequisites = [[5,8],[3,5],[1,9],[4,5],[0,2],[1,9],[7,8],[4,9]]
#     print(s.canFinish(numCourses, prerequisites))
#
# if __name__ == '__main__':
#     main()
