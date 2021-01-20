class Solution:
    def jump(self, nums):
        answer = 0
        index = 0
        index_max = len(nums)-1
        while index < index_max:
            value_tmp = -1
            if index + nums[index] >= index_max:
                    return answer+1
            else :
                for i in range(index+1,index+1+nums[index]):
                    if i + nums[min(i,index_max)] > value_tmp and nums[min(i,index_max)] != 0:
                        value_tmp = i + nums[i]
                        index_tmp = i
            index = index_tmp
            answer +=1
        return answer
