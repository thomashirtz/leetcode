class Solution(object):
    def intToRoman(self, num):
        letters = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ""
        for letter, number in zip(letters, numbers):
            roman += letter * (num // number)
            num %= number
        return roman


examples = [3, 4, 9, 58, 1994]
for example in examples:
    print(Solution().intToRoman(example))
