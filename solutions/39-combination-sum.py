class Solution:
    def __init__(self):
        self.answer = []
        self.target = None

    def combinationSum(self, candidates, target):
        self.target = target
        self.DFS(candidates, answer_=[], total_=0, index_=0)
        return self.answer

    def DFS(self, candidates, answer_, total_, index_):
        if total_ > self.target:
            pass
        elif total_ == self.target:
            self.answer.append(answer_)
        elif total_ < self.target:
            for i, candidate in enumerate(candidates[index_:]):
                self.DFS(candidates[index_:], answer_ + [candidate], total_ + candidate, i)
