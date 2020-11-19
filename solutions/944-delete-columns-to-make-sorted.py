class Solution:
    def minDeletionSize(self, A):
        array = map(list, zip(*A))
        answer = 0
        for row in array:
            if row != sorted(row):
                answer += 1
        return answer
