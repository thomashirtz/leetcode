class Solution:
    def firstMissingPositive(self, nums):
        nums.append(0)
        length = len(nums)

        for i in range(length):
            if nums[i] >= length or nums[i] < 0:
                nums[i] = 0

        for i in range(length):
            nums[nums[i] % length] += length

        for i in range(length):
            if not nums[i] // length:
                return i

        return length
