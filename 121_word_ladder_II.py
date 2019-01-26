'''
Given two words (start and end), and a dictionary,
find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
Notice

All words have the same length.
All words contain only lowercase alphabetic characters.

Example
Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
'''
from collections import deque, defaultdict
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, dictionary):

        results = []
        words_distance = defaultdict(int) # a dict to store word(key) and distance from end
        next_words_mapping = defaultdict(list) # a dict to store word(key) and set of next words (value)
        dictionary.add(start) # add the start to dictionary (must-do)
        dictionary.add(end) # add the end to dictionary (must-do)
        path = []
        # use bfs from end to start to get number of each word's transformation
        self.bfs(start, end, dictionary, words_distance, next_words_mapping)
        # use dfs from start to end to get all the result
        self.dfs(start, end, path, words_distance, next_words_mapping, results)

        return results


        def bfs(self, start, end, dictionary, words_distance, next_words_mapping):
            '''
            use BFS to traverse all word transformation from end to begin.
            store the distance (the step of transformation)
            for each word in Dictionary/Hash Map, called words_distance
            words_distance = {word: distance, ...}
            next_words_mapping = {word: [next_word1, next_word2,...]}
            '''

            queue = deque([end])
            visited_words = set([end])
            distance = 0

            while queue:
                size = len(queue)

                # traverse by level
                for i in range(size):
                    word = queue.popleft()
                    words_distance[word] = distance

                    next_words = self._get_next_words(word, dictionary)
                    next_words_mapping[word] = next_words

                    for next_word in next_words:
                        if next_word not in visited_words:
                            queue.append(next_word)
                            visited_words.add(next_word)
                distance += 1


        def _get_next_words(self, word, dictionary):

            next_words = []
            NUM_OF_ALPHABETS = 26

            for i in range(len(word)):
                for j in range(NUM_OF_ALPHABETS - 1):
                    index = (ord(word[i]) + j - ord('a')) % NUM_OF_ALPHABETS + ord('a')
                    new_char = chr(index)
                    new_word = self._replace_char(i,new_char, word)

                    if new_word in dictionary:
                        next_words.append(new_word)

            return next_words

        def _replace_char(self, i, char, word):
            return word[ : i] + char + word[i + 1 : ]


    def dfs(self, current_word, end, path, words_distance, next_words_mapping, results):
        '''
        use DFS to traverse each word and next word recursively, following the distance
        '''
        if current_word == end:
            path.append(end)
            results.append(path.copy())
            path.pop()
            return

        for next_word in next_words_mapping[current_word]:
            if words_distance[current_word] == words_distance[next_word] + 1:
                path.append(current_word)
                self.dfs(next_word, end, path, words_distance, next_words_mapping, results)
                path.pop()





# def main():
#     '''
#     start = "hit"
#     end = "cog"
#     dict = ["hot","dot","dog","lot","log"]
#     Return
#       [
#         ["hit","hot","dot","dog","cog"],
#         ["hit","hot","lot","log","cog"]
#       ]
#     '''
#     s = Solution()
#     start = "hit"
#     end = "cog"
#     dictionary = set(["hot","dot","dog","lot","log"])
#     print(s.findLadders(start, end, dictionary))
#
#     start = "hot"
#     end = "dog"
#     dictionary = set(["hot","cog","dog","tot","hog","hop","pot","dot"])
#     print(s.findLadders(start, end, dictionary))
#
# if __name__ == '__main__':
#     main()
