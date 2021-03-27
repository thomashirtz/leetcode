from math import ceil
from collections import Counter


class Solution:
    def numRabbits(self, answers):
        counter = dict(Counter(answers))
        answer = 0
        for key, value in counter.items():
            print(answer, key, value)
            answer += (key + 1) * ceil(value / (key + 1))
        return answer
