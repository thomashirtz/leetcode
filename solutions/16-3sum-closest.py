from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                if abs(tmp - target) < abs(answer - target):
                    answer = tmp

                if tmp > target:
                    right -= 1
                elif tmp < target:
                    left += 1
                else:
                    return target
        return answer
