class Solution:
    def numJewelsInStones(self, J, S):
        answer = 0
        for s in S:
            if s in J:
                answer += 1
        return answer
