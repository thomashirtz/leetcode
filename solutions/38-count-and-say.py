from itertools import groupby

class Solution:
    def countAndSay(self, n):
        result = "1"
        for _ in range(n - 1):
            tmp = ''
            for digit, group in groupby(result):
                count = len(list(group))
                tmp += f"{count}{digit}"
            result = tmp

        return result
