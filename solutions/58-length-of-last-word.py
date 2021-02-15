class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.rstrip(' ').split(' ')
        return len(l[-1])
