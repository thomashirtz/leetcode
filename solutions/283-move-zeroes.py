class Solution:
    def moveZeroes(self, nums):
        length, i,j = len(nums), 0, 0
        for i in range(length):
            if nums[i]!=0:
                if j<length:
                    nums[j]=nums[i]
                    j+=1
        nums[j:] = [0]*(length-j)
        return nums