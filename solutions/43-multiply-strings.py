class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        answer = [0] * (len(num1) + len(num2))

        for i, d1 in enumerate(reversed(num1)):
            for j, d2 in enumerate(reversed(num2)):
                answer[i + j] += int(d1) * int(d2)
                answer[i + j + 1] += answer[i + j] // 10
                answer[i + j] %= 10

        return ''.join(map(str, reversed(answer))).lstrip('0')
