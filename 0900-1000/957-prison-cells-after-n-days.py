from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        memory = []
        for i in range(N):
            cells = self.next_state(cells)
            if tuple(cells) in memory:
                return list(memory[N % len(memory) - 1])
            memory.append(tuple(cells))
        return cells

    def next_state(self, cells):
        cells_ = [0] * 8
        for i in range(1, len(cells) - 1):
            cells_[i] = int(cells[i - 1] == cells[i + 1])
        return cells_


examples = [[[0, 1, 0, 1, 1, 0, 0, 1], 21],
            [[1, 0, 0, 1, 0, 0, 1, 0], 1000000000]]

for example in examples:
    print(Solution().prisonAfterNDays(*example))