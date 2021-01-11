import collections


class Solution:
    def fourSum(self, nums, target):
        def findNSum(nums, N, target, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
                return
            if N == 2:
                left, right = 0, len(nums) - 1
                while left < right:
                    tmp = nums[left] + nums[right]
                    if tmp == target:
                        results.append(result + [nums[left], nums[right]])
                        left += 1
                    elif tmp > target:
                        right -= 1
                    else:
                        left += 1
            else:
                for i in range(len(nums) - N + 1):
                    findNSum(nums[i + 1:], N - 1, target - nums[i], result + [nums[i]], results)

        results = []
        findNSum(sorted(nums), 4, target, [], results)

        clean_results = []
        for x in results:
            if sorted(x) not in clean_results:
                clean_results.append(sorted(x))
        return clean_results