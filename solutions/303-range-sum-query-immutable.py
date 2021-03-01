class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        self.create_lookuptable()

    def create_lookuptable(self):
        self.lookuptable = [0]
        for i in range(len(self.nums)):
            self.lookuptable.append(self.lookuptable[i] + self.nums[i])

    def sumRange(self, i, j):
        return self.lookuptable[j + 1] - self.lookuptable[i]
