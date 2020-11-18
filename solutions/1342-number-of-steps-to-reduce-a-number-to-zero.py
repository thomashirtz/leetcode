class Solution:
    def numberOfSteps (self, num: int):
        digits = f'{num:b}'
        return len(digits) + digits.count('1') - 1