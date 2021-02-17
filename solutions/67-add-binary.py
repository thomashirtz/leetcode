class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry, result = 0, ''
        a, b = list(a), list(b)
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            result = str(carry % 2) + result
            carry //= 2
        return result
