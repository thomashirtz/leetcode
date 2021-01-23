class Solution:
    def search(self, nums, target) -> int:
        start, end = 0, len(nums) - 1
        while start < end:
            middle = (start + end) // 2
            if nums[middle] > nums[end]:
                start = middle + 1
            else:
                end = middle

        index_rotation = start
        start, end = 0, len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            real_middle = (middle + index_rotation) % len(nums)
            if nums[real_middle] == target:
                return real_middle
            elif nums[real_middle] < target:
                start = middle + 1
            else:
                end = middle - 1
        return -1
