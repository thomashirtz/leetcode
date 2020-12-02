class Solution:
    def __init__(self):
        self.answer = []

    def subsets(self, nums, path=[]):
        self.answer.append(path)
        for i in range(len(nums)):
            self.subsets(nums[i + 1:], path + [nums[i]])
        return self.answer