'''
Given a list of words and an integer k, return the top k frequent words in the list.

Notice

You should order the words by the frequency of them in the return list,
the most frequent one comes first. If two words has the same frequency,
the one with lower alphabetical order come first.

Example
Given

[
    "yes", "lint", "code",
    "yes", "code", "baby",
    "you", "baby", "chrome",
    "safari", "lint", "code",
    "body", "lint", "code"
]
for k = 3, return ["code", "lint", "baby"].

for k = 4, return ["code", "lint", "baby", "yes"],
'''
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    """
    @param: words: an array of string
    @param: k: An integer
    @return: an array of string
    """
    def topKFrequentWords__max_heap(self, words, k):
        '''
        idea:
        1. Use the hash map (dict) to calculate the frequency of each word.
        push each word and its frequency into max heap, (frequency, word)
        pop k words from max heap and append(push) into result(list).

        Time: O(klogn)

        2. use min heap
        Time O(nlogk)
        '''

        result = []

        words_count = defaultdict(int)
        for word in words:
            words_count[word] += 1

        max_heap = []
        for word in words_count:
            count = words_count[word]
            heappush(max_heap, (-count, word))

        for i in range(k):
            count, word = heappop(max_heap)
            result.append(word)

        return result


    def topKFrequentWords__min_heap(self, words, k):
        if not words or k == 0:
            return []

        result = []
        words_count = defaultdict(int)

        for word in words:
            words_count[word] += 1

        min_heap = []
        for word in words_count:
            count = words_count[word]
            heappush(min_heap, Item(count, word))

            if len(min_heap) > k:
                heappop(min_heap)

        while min_heap:
            result.append(heappop(min_heap).word)

        result.reverse()

        return result


class Item:
    def __init__(self, count, word):
        self.count = count
        self.word = word


    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word

        return self.count < other.count


    def __gt__(self, other):
        if self.count == other.count:
            return self.word < other.word

        return self.count > other.count


    def __eq__(self, other):
        return self.count == other.count and self.word == other.word
# def main():
#     s = Solution()
#     words = ["yes", "lint", "code",
#             "yes", "code", "baby",
#             "you", "baby", "chrome",
#             "safari", "lint", "code",
#             "body", "lint", "code"]
#     k = 3
#     print(s.topKFrequentWords(words, k) == ["code", "lint", "baby"])
#
#     k = 4
#     print(s.topKFrequentWords(words, k) == ["code", "lint", "baby", "yes"])
#
#
# if __name__ == '__main__':
#     main()
