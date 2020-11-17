class Solution:
    def restoreString(self, s: str, indices) -> str:
        answer = ['']*len(s)
        for i, c in zip(indices, s):
            answer[i] = c
        return ''.join(answer)