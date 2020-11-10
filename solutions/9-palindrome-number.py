class Solution:
    def isPalindrome(self, x):
        x = str(x)
        for i in range(len(x)//2):
            if x[i] != x[~i]:
                return False
        return True