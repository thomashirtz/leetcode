class Solution:
    def searchRange(self, nums, target):

        def search_left(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                middle = (left + right) // 2
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle
            return left if nums[left] == target else -1

        def search_right(nums, target):
            left, right = 0, len(nums) - 1
            while left < right:
                middle = (left + right) // 2 + 1
                if nums[middle] > target:
                    right = middle - 1
                else:
                    left = middle
            return left if nums[left] == target else -1

        return [search_left(nums, target), search_right(nums, target)]