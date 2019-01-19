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
        top_5_scores = defaultdict(list)
        for record in records:
            top_5_scores[record.id].append(record.score)

        top_5_avg_scores = {}
        for id in top_5_scores:
            top_5_scores[id].sort()
            top_5_avg_scores[id] = sum(top_5_scores[id][-5:]) / 5

        return top_5_avg_scores


    def highFive2(self, records):
        if not results:
            return {}

        top_5_scores = defaultdict(list)
        '''
        { id1: [score1, score2, score3, score4, score5],
          id2: [score1, score2, score3, score4, score5],
          ...
        }
        '''
        for record in records:
            heappush(top_5_scores[record.id], record.score)

            if (len(top_5_scores[record.id])) > 5:
                heappop(top_5_scores[record.id])

            # From line 50 to 53 is euqal to from line 57 to 62

            # if len(top_5_scores[record.id]) < 5:
            #     heappush(top_5_scores[record.id], record.score)
            # else:
            #     if record.score > top_5_scores[record.id][0]:
            #         heappop(top_5_scores[record.id])
            #         heappush(top_5_scores[record.id], record.score)

        top_5_avg_scores = defaultdict(float)
        for id in top_5_scores:
            top_5_avg_scores[id] = sum(top_5_scores[id]) / 5
        return top_5_avg_scores


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
