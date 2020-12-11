class Solution:
    def isHappy(self, x):

        def function(number):
            squares = 0
            while number:
                squares += (number % 10) ** 2
                number = number // 10
            return squares

        y = x
        while True:
            x = function(x)
            if x == 1: return True
            y = function(function(y))
            if x == y: return False