class Solution:
    def searchInsert(self, nums, target) -> int:
        start, end = 0, len(nums)
        while start < end:
            middle = (start + end)//2
            if target <= nums[middle]:
                end = middle
            else:
                start = middle + 1
        return start