class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)

# https://leetcode.com/problems/maximum-subarray/discuss/20396/Easy-Python-Way
# I was quite impressed by the solution, so I did just keep it for this problem ..
