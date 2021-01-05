class Solution:
    def lengthOfLongestSubstring(self, string):
        used = {}
        start, length = 0, 0

        for i, c in enumerate(string):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                length = max(length, i - start + 1)
            used[c] = i
        return length
