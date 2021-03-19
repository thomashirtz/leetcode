class Solution:
    def countBinarySubstrings(self, s):
        array = list(map(len, s.replace('01', '0 1').replace('10', '1 0').split()))
        return sum(min(a, b) for a, b in zip(array, array[1:]))
