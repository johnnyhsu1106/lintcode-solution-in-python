'''
Given a matrix of lower alphabets and a dictionary.
Find all words in the dictionary that can be found in the matrix.
A word can start from any position in the matrix and go left/right/up/down to the adjacent position.


Have you met this question in a real interview? Yes
Example
Given matrix:
doaf
agai
dcan
and dictionary:
{"dog", "dad", "dgdg", "can", "again"}

return {"dog", "dad", "can", "again"}

Challenge
Using trie to implement your algorithm.
'''

class TrieNode:
    def __init__(self):
        self.word = ''
        self.children = dict()
        self.is_complete_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            child = node.children.get(char)
            if not child:
                child = TrieNode()
                node.children[char] = child
            node = child
        node.is_complete_word = True
        node.word = word

    # def startWith(self, prefix):
    #     node = self.root
    #     for char in prefix:
    #         child = node.children[char]
    #         if not child:
    #             return False
    #         node = child
    #     return True
    #
    # def search(self, word):
    #     node = self.root
    #     for char in word:
    #         child = node.children.get(char)
    #         if not child:
    #             return False
    #         node = child
    #     return node.is_complete_word


class Solution:
    """
    @param: board: A list of lists of character
    @param: words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if not board or len(board) == 0 or len(board[0]) == 0 or len(words) == 0:
            return []

        result = []
        trie = Trie()
        for word in words:
            trie.insert(word)

        m, n = len(board), len(board[0])
        for x in range(m):
            for y in range(n):
                word = board[x][y]
                self.search_dfs(board, x, y, trie.root, result)
        return result


    def search_dfs(self, board, x, y, node, result):

        if node.is_complete_word:
            word = node.word
            if word not in result:
                result.append(word)


        if self.is_bound(x, y, board):
            child = node.children.get(board[x][y])

            if child:
                dx = [1, -1, 0, 0]
                dy = [0, 0, 1, -1]

                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]

                    char = board[x][y]
                    board[x][y] = '#'
                    self.search_dfs(board, new_x, new_y, child, result)
                    board[x][y] = char


    def is_bound(self, x, y, board):
        m, n = len(board), len(board[0])
        return 0 <= x <= m - 1 and 0 <= y <= n - 1


# def main():
#     s = Solution()
#     board = [['d','o','a','f'],
#              ['a','g','a','i'],
#              ['d','c','a','n']]
#     words = ["dog", "dad", "dgdg", "can", "again"]
#     print(s.wordSearchII(board, words))
#
# if __name__ == '__main__':
#     main()
