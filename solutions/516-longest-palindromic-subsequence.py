class Solution:
    def longestPalindromeSubseq(self, s):
        LPS = {}

        def recursion(s):
            if s not in LPS:
                max_length = 0
                for c in set(s):
                    i, j = s.find(c), s.rfind(c)
                    max_length = max(max_length, 1 if i==j else 2+recursion(s[i+1:j]))
                LPS[s] = max_length
            return LPS[s]
        return recursion(s)
