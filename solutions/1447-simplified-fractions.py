from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        answer = []
        set_ = set()
        for denominator in range(1,n+1):
            for numerator in range(1,n):
                if numerator/denominator<1 and numerator/denominator not in set_:
                    answer.append(f'{numerator}/{denominator}')
                    set_.add(numerator/denominator)
        return answer


examples = [1, 2, 3, 4]
for example in examples:
    print(Solution().simplifiedFractions(example))
