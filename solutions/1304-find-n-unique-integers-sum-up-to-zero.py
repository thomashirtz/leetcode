class Solution:
    def sumZero(self, n):
        return range(-n + 1, n, 2)


examples = [5, 3, 1]
for example in examples:
    print(f'{example} {list(Solution().sumZero(example))}', sep='\n\n')