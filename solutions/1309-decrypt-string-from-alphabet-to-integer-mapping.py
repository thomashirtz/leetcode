import re

class Solution:
    def freqAlphabets(self, s: str) -> str:
        return ''.join(chr(int(number[:2])+96) for number in re.findall(r'\d\d#|\d', s))