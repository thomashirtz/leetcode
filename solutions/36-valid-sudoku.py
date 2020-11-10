from collections import Counter


class Solution:
    def isValidSudoku(self, board):
        for i in range(9):
            counter_row = Counter()
            counter_column = Counter()
            for j in range(9):
                if counter_row[board[i][j]] == 1 or counter_column[board[j][i]] == 1:
                    return False
                if board[i][j] != '.':
                    counter_row[board[i][j]]+=1
                if board[j][i] != '.':
                    counter_column[board[j][i]]+=1
        for x in [0,3,6]:
            for y in [0,3,6]:
                counter = Counter()
                for i in range(x,x+3):
                    for j in range(y,y+3):
                        if counter[board[i][j]]==1:
                            return False
                        if board[i][j] != '.':
                            counter[board[i][j]]+=1
        return True
