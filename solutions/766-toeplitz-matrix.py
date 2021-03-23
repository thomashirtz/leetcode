class Solution:
    def isToeplitzMatrix(self, matrix):
        M, N = len(matrix[0]), len(matrix)
        if M == 1 or N == 1:
            return True
        
        for i in range(M):
            for j in range(min(N, M - i)):
                if j == 0:
                    tmp = matrix[j][i + j]
                else:
                    if tmp != matrix[j][i + j]:
                        return False

        for j in range(1, N):
            for i in range(min(N - j, M)):
                if i == 0:
                    tmp = matrix[j + i][i]
                else:
                    if tmp != matrix[j + i][i]:
                        return False

        return True
