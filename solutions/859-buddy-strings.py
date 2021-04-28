class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        tmp = [[a, b] for a, b in zip(A, B) if a != b]
        if tmp == [] and len(A) != len(set(A)):
            return True
        if len(tmp) == 2 and tmp[0] == tmp[1][::-1]:
            return True
        return False
