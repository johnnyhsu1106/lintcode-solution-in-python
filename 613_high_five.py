'''
There are two properties in the node student id and scores,
to ensure that each student will have at least 5 points,
find the average of 5 highest scores for each person.

Have you met this question in a real interview? Yes
Example
Given results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]

Return
'''

# Definition for a Record
class Record:
    def __init__(self, id, score):
        self.id = id
        self.score = score

from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive1(self, records):
        scores = defaultdict(list)
        for record in records:
            scores[record.id].append(record.score)

        scores_avg = {}
        for id in scores:
            scores[id].sort()
            scores_avg[id] = float(sum(scores[id][-5:])) / 5

        return scores_avg


    def highFive2(self, records):
        scores = defaultdict(list)

        for record in records:
            heappush(scores[record.id], record.score)
            if (len(scores[record.id])) > 5:
                heappop(scores[record.id])
            # from line 42 to line 44 is equal to the line 47 to 54

            # if len(scores[record.id]) < 5:
            #     heappush(scores[record.id], record.score)
            # else:
            #
            #     if record.score > scores[record.id][0]:
            #         heappop(scores[record.id])
            #         heappush(scores[record.id], record.score)
        scores_avg = {}
        for id in scores:
            scores_avg[id] = sum(scores[id]) / 5.0
        return scores_avg


# def main():
#     s = Solution()
#     results = [Record(1, 91), Record(1, 92), Record(2, 93), Record(2, 99), Record(2, 98),
#              Record(2, 97), Record(1, 60), Record(1, 58), Record(2, 100), Record(1, 61),
#             Record(1,100), Record(2, 87)]
#
#     print(s.highFive1(results))
#     print(s.highFive2(results))
#
#
# if __name__ == '__main__':
#     main()
