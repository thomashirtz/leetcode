from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        counter = {v: [0] * len(votes[0]) + [v] for v in votes[0]}
        for vote in votes:
            for i, team in enumerate(vote):
                counter[team][i] -= 1
        return ''.join(sorted(counter.keys(), key=counter.get))


examples = [
    ["ABC", "ACB", "ABC", "ACB", "ACB"],  # ACB
    ["WXYZ", "XYZW"],  # XWYZ
    ["ZMNAGUEDSJYLBOPHRQICWFXTVK"],  # ZMNAGUEDSJYLBOPHRQICWFXTVK
    ["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"],  # ABC
    ["M", "M", "M", "M"],  # M
    ["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]  # ABC
]

for example in examples:
    print(Solution().rankTeams(example))