'''
Given a 2D grid,
each cell is either a wall 'W', an enemy 'E' or empty '0'(the number zero),
return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column
from the planted point until it hits the wall since the wall is too strong to be destroyed.

Notice

You can only put the bomb at an empty cell.

Example
Given a grid:

0 E 0 0
E 0 W E
0 E 0 0
return 3. (Placing a bomb at (1,1) kills 3 enemies)
'''

class Solution:
    """
    @param: grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    # def maxKilledEnemies(self, grid):
    #     if grid is None or len(grid) == 0 or len(grid[0]) == 0:
    #         return 0
    #
    #     m, n = len(grid), len(grid[0])
