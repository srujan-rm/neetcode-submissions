class Solution:
    def __init__(self):
        self.dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.word = None
    def explore(self, i, j, board, trace, letters_remaining):
        letters_used = len(self.word) - letters_remaining
        trace.append(board[i][j])
        old_val = board[i][j]
        board[i][j] = '-'
        if (letters_remaining == 0):
            trace.pop()
            board[i][j] = old_val 
            return True
        for u, v in self.dirs:
            _i, _j = i + u, j + v
            if (_i < 0) or (_j < 0) or (_i >= len(board)) or (_j >= len(board[0])):
                continue 
            if (board[_i][_j] == '-' or board[_i][_j] != self.word[letters_used]):
                continue
            possibility = self.explore(_i, _j, board, trace, letters_remaining - 1)
            if (possibility):
                trace.pop()
                board[i][j] = old_val 
                return True
        trace.pop()
        board[i][j] = old_val 
        return False
        
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        letters_remaining = len(word)
        self.word = word
        m, n = len(board), len(board[0])
        for i in range(0, m):
            for j in range(0, n):
                if board[i][j] == word[0][0]:
                    trace = []
                    check = self.explore(i, j, board, trace, letters_remaining - 1)
                    if (check):
                        return True
        return False