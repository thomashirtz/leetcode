from math import ceil

class Solution:
    def minEatingSpeed(self, piles, H):
        left, right = ceil(sum(piles)/H), max(piles)
        while left < right:
            middle = (right+left) // 2
            somme = sum(-(-pile//middle) for pile in piles)
            if somme > H:
                left = middle +1
            else :
                right = middle
        return left