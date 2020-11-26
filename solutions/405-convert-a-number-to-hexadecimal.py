class Solution:
    def toHex(self, num: int) -> str:
        if num < 0:
            num += 2**32
        if num == 0:
            return "0"
        conversion = "0123456789abcdef"
        answer = ""
        while num > 0:
            remainder = num % 16
            num //= 16
            answer += conversion[remainder]
        return answer[::-1]


examples = [26, 10, -1, 16]
for example in examples:
    print(Solution().toHex(example))