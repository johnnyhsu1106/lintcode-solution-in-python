'''
Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0
(the number zero, one, two).
Zombies can turn the nearest people(up/down/left/right) into zombies every day,
but can not through wall.
How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.

Example
Given a grid:

0 1 2 0 0
1 0 0 2 1
0 1 0 0 0
return 2
'''

PEOPLE = 0
ZOMBIE = 1
WALL = 2

from collections import deque
class Solution:
    """
    @param: grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):

        days = 0
        people = 0
        m = len(grid)
        n = len(grid[0])

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        for x in range(m):
            for y in range(n):
                if grid[x][y] == ZOMBIE:
                    queue.append((x, y))
                elif grid[x][y] == PEOPLE:
                    people += 1
        # edge case
        if people == 0:
            return -1

        queue = deque()
        while queue:
            days += 1
            size = len(queue)
            #  traverse each level
            for i in range(size): # for all zombie in the queue
                (x, y) = queue.popleft()
                
                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]

                    if self.is_people_bound(new_x, new_y, grid):
                        grid[new_x][new_y] = ZOMBIE
                        people -= 1
                        queue.append((new_x, new_y))

                    if people == 0:
                        return days
        return -1


    def is_people_bound(self, x, y, grid):
        m = len(grid)
        n = len(grid[0])
        return 0 <= x <= m -1 and 0 <= y <= n - 1 and grid[x][y] == PEOPLE



# def main():
#     s = Solution()
#     grid = [ [0, 1, 2, 0, 0],
#                [1, 0, 0, 2, 1],
#                [0, 1, 0, 0, 0]]
#     print(s.zombie(grid))
#
# if __name__ == '__main__':
#     main()
