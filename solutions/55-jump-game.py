class Solution:
    def canJump(self, nums):
        maximum_distance = 0
        for i, num in enumerate(nums):
            if i > maximum_distance:
                return False
            maximum_distance = max(maximum_distance, i + num)
        return True
