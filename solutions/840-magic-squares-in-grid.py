class Solution:
    def numMagicSquaresInside(self, grid):
        n, m, answer = len(grid), len(grid[0]), 0
        magic_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

        def is_magic(grid):
            if 15 == sum(grid[k][k] for k in range(3)):
                if set(grid[0] + grid[1] + grid[2]) == magic_set:
                    if [15] * 3 == list(map(sum, grid)):
                        if [15] * 3 == list(map(sum, map(list, zip(*grid)))):
                            return 1
            return 0

        for j in range(n - 2):
            for i in range(m - 2):
                sub_grid = [grid[j + k][i:i + 3] for k in range(3)]
                answer += is_magic(sub_grid)

        return answer
