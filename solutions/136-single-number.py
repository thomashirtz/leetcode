class Solution:
    def singleNumber(self, nums):
        answer = []
        for num in nums:
            if num not in answer:
                answer.append(num)
            else:
                answer.remove(num)
        return answer[0]