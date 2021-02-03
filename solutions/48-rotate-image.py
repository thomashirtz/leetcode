class Solution:
    def rotate(self, matrix):
        length = len(matrix)
        for i in range(length//2):
            for j in range(i, length-1-i):
                matrix[i][j], matrix[j][~i], matrix[~i][~j], matrix[~j][i] = \
                matrix[~j][i], matrix[i][j], matrix[j][~i], matrix[~i][~j]
