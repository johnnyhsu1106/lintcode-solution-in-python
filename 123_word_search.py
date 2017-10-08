'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Have you met this question in a real interview? Yes
Example
Given board =

[
  "ABCE",
  "SFCS",
  "ADEE"
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

class Solution:
    """
    @param: board: A list of lists of character
    @param: word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # edge case
        if not board or len(board) == 0 or len(board[0]) == 0:
            return False
        # edge case
        if len(word) == 0:
            return True

        m, n = len(board), len(board[0])
        for x in range(m):
            for y in range(n):
                if self.dfs(board, x, y, 0, word):
                    return True
        return False


    def dfs(self, board, x , y, index, word):
        # stopping case(base case)
        if index == len(word):
            return True
        # stopping case(base case)
        if not self.is_bound(x, y, board) or board[x][y] != word[index]:
            return False

        board[x][y] = '#' # avoid repeat do the DFS on the same location
        is_finded = self.dfs(board, x - 1, y, index + 1, word) or \
                    self.dfs(board, x + 1, y, index + 1, word) or \
                    self.dfs(board, x, y - 1, index + 1, word) or \
                    self.dfs(board, x, y + 1, index + 1, word)
        board[x][y] = word[index] # backtracking

        return is_finded


    def is_bound(self, x, y, board):
        m, n = len(board), len(board[0])
        return 0 <= x <= m - 1 and 0 <= y <= n - 1


# def main():
#     s = Solution()
#     board = [['A', 'B', 'C', 'E'],
#              ['S', 'F', 'C', 'S'],
#              ['A', 'D', 'E', 'E']]
#     print(board)
#     word = "ABCCED"
#     print(s.exist(board, word))
#     #
#     word = "SEE"
#     print(s.exist(board, word))
#     #
#     word = "ABCB"
#     print(s.exist(board, word))
#
# if __name__ == '__main__':
#     main()
