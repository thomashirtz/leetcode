class Solution:
    def countBits(self, num):
        array = [0]
        for i in range(1, num + 1):
            array.append(array[i // 2] + i % 2)
        return array
