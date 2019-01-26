'''
Given two words (start and end), and a dictionary,
find the length of shortest transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
Notice

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.

Example
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
'''
from collections import deque
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dictionary):
        '''
        idea:
        BFS
        Find the length of shortest transformation;
        Like Graph
        From one transformation to another transformation and
        find the shortest path to reach the goal
        '''
        if not start or not end or len(dictionary) == 0:
            return 0

        if start == end:
            return 1

        # use the bfs to tranverse all paths
        dictionary.add(end)
        queue = deque([start])
        visited_words = set([start])
        distance = 0

        while queue:
            distance += 1

            for i in range(len(queue)):
                word = queue.popleft()

                if word == end:
                    return distance

                next_words = self._get_next_words(word, dictionary)

                for next_word in next_words:
                    if next_word not in visited_words:
                        queue.append(next_word)
                        visited_words.add(next_word)


        return 0


    def _get_next_words(self, word, dictionary):
        next_words = []
        CHARS = 'abcdefghijklmnopqrstuvwxyz'

        for i in range(len(word)):
            for char in CHARS:
                if word[i] != char:
                    next_word = word[: i] + char + word[i + 1: ]

                    if next_word in dictionary:
                        next_words.append(next_word)

        return next_words



# def main():
#     s = Solution()
#     start = 'hit'
#     end = 'cog'
#     dictionary = set(["hot","dot","dog","lot","log"])
#     print(s.ladderLength(start, end , dictionary))
#
#     start = 'a'
#     end = 'c'
#     dictionary = set(['a', 'b', 'c'])
#
#     print(s.ladderLength(start, end , dictionary))
#
#
# if __name__ == '__main__':
#     main()
