import re
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph, banned):
        paragraph = re.sub('[^A-Za-z0-9\s]+', ' ', paragraph.lower()).split()
        counter = Counter(paragraph)
        for word in banned:
            del counter[word]
        return counter.most_common(1)[0][0]