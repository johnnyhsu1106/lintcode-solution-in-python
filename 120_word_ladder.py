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

        if start == end:
            return 1

        if len(dictionary) == 0:
            return 0

        #  add the end to the dictionary
        dictionary.add(start)
        dictionary.add(end)
        #  initialize the BFS (queue<deque> and visited<set>)
        queue = deque([start])
        visited_words = set([start])
        path = 0

        while queue:
            path += 1
            size = len(queue)

            for i in range(size):
                word = queue.popleft()
                if word == end:
                    return path

                words = self.get_next_words(word, dictionary)

                for new_word in words:
                    if new_word not in visited_words:
                        queue.append(new_word)
                        visited_words.add(new_word)

        return 0


    def get_next_words(self, word, dictionary):
        next_words = []

        for i in range(len(word)):
            for j in range(25):
                index = (ord(word[i]) + j - ord('a')) % 26 + ord('a')
                new_char = chr(index)
                next_word = self.replace_char(i, new_char, word)
                if next_word in dictionary:
                    next_words.append(next_word)

        return next_words


    def replace_char(self, replace_index, new_char, word):
        return word[:replace_index] + new_char + word[replace_index + 1:]
        # word_list = list(word)
        # word_list[replace_char] = new_char
        # return "".join(word_list)


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
