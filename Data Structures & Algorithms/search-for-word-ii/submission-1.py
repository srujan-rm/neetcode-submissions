class Node:
    def __init__(self):
        self.letter = [None for i in range(26)]
        self.end = False
        self.found = False

class PrefixTree:
    def __init__(self):
        self.head = Node()
    def insert(self, word: str) -> None:
        it, n, node_it = 0, len(word), self.head
        while it < n:
            index = ord(word[it]) - ord('a')
            if not node_it.letter[index]:
                node_it.letter[index] = Node() 
            node_it = node_it.letter[index] 
            it += 1
        node_it.end = True 
        
class Solution:
    def explore_more(self, board, storage, tail, obtained, dirs, i, j, word, remaining):
        old_value = board[i][j] 
        word.append(old_value)
        board[i][j] = '-'
        if tail.end and (not tail.found):
                obtained.append("".join(word))
                tail.found = True 
        if (remaining == 0):
            word.pop() 
            board[i][j] = old_value
            return
        for u, v in dirs:
            _i, _j = u + i, v + j
            if _i < 0 or _j < 0 or _i >= len(board) or _j >= len(board[0]):
                continue
            if board[_i][_j] == '-':
                continue
            if tail.letter[ord(board[_i][_j]) - ord('a')]:
                self.explore_more(board, storage, tail.letter[ord(board[_i][_j]) - ord('a')], obtained, dirs, _i, _j, word, remaining - 1) 
            else:
                continue 
        word.pop()
        board[i][j] = old_value
        
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        max_word_length = float("-inf")
        storage = PrefixTree()
        m, n = len(board), len(board[0])
        obtained = []
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for word in words:
            max_word_length = max(max_word_length, len(word))
            storage.insert(word)
        for i in range(m):
            for j in range(n):
                word = []
                if storage.head.letter[ord(board[i][j]) - ord('a')]:
                    self.explore_more(board, storage, storage.head.letter[ord(board[i][j]) - ord('a')], obtained, dirs, i, j, word, max_word_length - 1)
        return obtained
