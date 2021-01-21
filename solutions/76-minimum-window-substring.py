from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        i = start = end = 0

        for j, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            if not missing:
                while need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not end or j - i < end - start:
                    start, end = i, j
        return s[start: end]
