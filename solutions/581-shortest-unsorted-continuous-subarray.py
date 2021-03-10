class Solution:
    def findUnsortedSubarray(self, nums):
        answer = []
        for i, (a, b) in enumerate(zip(nums, sorted(nums))):
            if a != b:
                answer.append(i)
        if not answer:
            return 0
        else:
            return answer[-1]-answer[0]+1
