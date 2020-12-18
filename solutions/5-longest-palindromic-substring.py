class Solution:
    def longestPalindrome(self, string: str) -> str:
        palindrome = ""
        for i in range(len(string)):
            palindrome = max(self.helper(string, i, i), self.helper(string, i, i + 1), palindrome, key=len)
        return palindrome

    def helper(self, string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return string[left + 1: right]
