'''
Given two words (start and end), and a dictionary,
find all shortest transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
 Notice

All words have the same length.
All words contain only lowercase alphabetic characters.
Have you met this question in a real interview? Yes
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

        result = []
        distances = defaultdict(int) # a dict to store word(key) and distance from end
        mapping = defaultdict(list) # a dict to store word(key) and set of next words (value)
        dictionary.add(start) # add the start to dictionary (must-do)
        dictionary.add(end) # add the end to dictionary (must-do)

        self.bfs(start, end, dictionary, distances, mapping)
        self.dfs(start, end, [], distances, mapping, result)

        return result


    def dfs(self, current_word, end, path, distances, mapping, result):
        '''
        use DFS to traverse each word and next word recursively, following the distance
        '''
        if current_word == end:
            path.append(end)
            result.append(list(path))
            path.pop()
            return

        for next_word in mapping[current_word]:
            if distances[current_word] == distances[next_word] + 1:
                path.append(current_word)
                self.dfs(next_word, end, path, distances, mapping, result)
                path.pop()


    def bfs(self, start, end, dictionary, distances, mapping):
        '''
        use BFS to traverse all word transformation from end to begin.
        store the distance (the step of transformation)
        for each word in Dictionary/Hash Map, called distances
        distances = {word: distance, ...}
        mapping = {word: [next_word1, next_word2,...]}
        '''

        queue = deque([end])
        visited = set([end])
        distance = 0

        while queue:
            size = len(queue)

            # traverse by level
            for i in range(size):
                word = queue.popleft()
                distances[word] = distance

                next_words = self.get_next_words(word, dictionary)
                mapping[word] = next_words

                for next_word in next_words:
                    if next_word not in visited:
                        queue.append(next_word)
                        visited.add(next_word)
            distance += 1


    def get_next_words(self, word, dictionary):

        next_words = []
        for i in range(len(word)):
            for j in range(25):
                index = (ord(word[i]) + j - ord('a')) % 26 + ord('a')
                new_char = chr(index)
                new_word = self.replace_char(i,new_char, word)

                if new_word in dictionary:
                    next_words.append(new_word)

        return next_words

    def replace_char(self, i, char, word):
        return word[:i] + char + word[i + 1:]


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
