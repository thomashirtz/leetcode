class Solution:
    def majorityElement(self, nums):
        counter, candidate = 0, None
        for num in nums:
            if not counter:
                counter = 1
                candidate = num
            else:
                if num == candidate:
                    counter += 1
                else:
                    counter -= 1
        return candidate