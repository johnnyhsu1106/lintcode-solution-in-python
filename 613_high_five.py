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
class Solution:
    # @param {Record[]} results a list of <student_id, score>
    # @return {dict(id, average)} find the average of 5 highest scores for each person
    # <key, value> (student_id, average_score)
    def highFive(self, records):
        scores =defaultdict(list)
        for record in records:
            scores[record.id].append(record.score)

        scores_avg = {}
        for id in scores:
            scores[id].sort()
            scores_avg[id] = float(sum(scores[id][-5:])) / 5
        return scores_avg

# def main():
#     s = Solution()
#     results = [[1,91],[1,92],[2,93],[2,99],[2,98],[2,97],[1,60],[1,58],[2,100],[1,61]]
#     print(s.highFive(results))
#
#
# if __name__ == '__main__':
#     main()
