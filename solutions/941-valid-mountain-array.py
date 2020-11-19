class Solution:
    def validMountainArray(self, A):
        if len(A) < 3 or A == sorted(list(A)) or A[::-1] == sorted(list(A)):
            return False
        l = A.index(max(A))+1
        return A[:l] == sorted(list(A[:l])) and A[l-1:][::-1] == sorted(list(A[l-1:]))
