class Solution:
    def reverse(self, x: int):
        signe = [1,-1][x < 0]
        x = x*signe
        x = int(str(x)[::-1])
        return x*signe*(x < 2**31)


examples = [123, -123, 120, 0]

for example in examples:
    print(Solution().reverse(example))