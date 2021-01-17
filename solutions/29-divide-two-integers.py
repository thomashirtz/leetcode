class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            temp, i = divisor, 1
            while temp <= dividend:
                dividend -= temp
                quotient += i
                temp = temp << 1
                i = i << 1

        quotient = quotient if positive else -quotient
        return min(max(-2147483648, quotient), 2147483647)
