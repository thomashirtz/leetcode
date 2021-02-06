from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        answer = []
        m, n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m - 1, 0, n - 1

        while up < down and left < right:
            answer.extend([matrix[up][i] for i in range(left, right)])
            answer.extend([matrix[i][right] for i in range(up, down)])
            answer.extend([matrix[down][i] for i in range(right, left, -1)])
            answer.extend([matrix[i][left] for i in range(down, up, -1)])
            up, down, left, right = up + 1, down - 1, left + 1, right - 1

        if left == right:
            answer.extend([matrix[i][right] for i in range(up, down + 1)])

        elif up == down:
            answer.extend([matrix[up][i] for i in range(left, right + 1)])

        return answer
