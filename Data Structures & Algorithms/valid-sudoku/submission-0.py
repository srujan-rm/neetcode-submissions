class Solution:
    def details(self, i, j):
        grid_col = -1
        grid_row = -1
        if (j in {0, 1, 2}):
            grid_col = 0
        elif (j in {3, 4, 5}):
            grid_col = 1
        else:
            grid_col = 2
        
        if (i in {0, 1, 2}):
            grid_row = 0
        elif (i in {3, 4, 5}):
            grid_row = 1
        else:
            grid_row = 2
        return (i, j, grid_row * 3 + grid_col)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_validity = [[0] * 9 for i in range(9)]
        col_validity = [[0] * 9 for i in range(9)]
        grid_validity = [[0] * 9 for i in range(9)]
        m, n = 9, 9
        for i in range(m):
            for j in range(n):
                if (board[i][j] == '.'):
                    continue
                row, col, grid = self.details(i, j)
                element = int(board[i][j]) - 1
                if (row_validity[row][element] == 0):
                    row_validity[row][element] = 1
                else:
                    return False
                if (col_validity[col][element] == 0):
                    col_validity[col][element] = 1
                else:
                    return False
                if (grid_validity[grid][element] == 0):
                    grid_validity[grid][element] = 1 
                else:
                    return False
        return True