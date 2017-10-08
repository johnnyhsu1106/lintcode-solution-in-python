'''
Merge two given sorted integer array A and B into a new sorted integer array.

Example
A=[1,2,3,4]

B=[2,4,5,6]

return [1,2,2,3,4,4,5,6]

Challenge
How can you optimize your algorithm if one array is very large and the other is very small?
'''
class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        result = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                result.append(A[i])
                i += 1
            else:
                result.append(B[j])
                j += 1
                
        # Time: O(k), Space: None
        while i < len(A):
            result.append(A[i])
            i += 1

        while j < len(B):
            result.append(B[j])
            j += 1

        # Option 1
        # Time: O(2k), Space: O(k)
        # if i == len(A):
        #     result.extend(B[j:])
        # else:
        #     result.extend(A[i:])

        return result
