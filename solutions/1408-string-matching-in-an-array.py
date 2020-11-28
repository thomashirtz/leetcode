from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []
        words.sort(key=len)
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    answer.append(words[i])
                    break
        return answer


examples = [
    ["mass", "as", "hero", "superhero"],
    ["leetcode", "et", "code"],
    ["leetcoder", "leetcode", "od", "hamlet", "am"]
]
for example in examples:
    print(Solution().stringMatching(example))