class Node:
    def __init__(self):
        self.letter = [None for i in range(26)]
        self.end = False

class WordDictionary:

    def __init__(self):
        self.head = Node() 
    def addWord(self, word: str) -> None:
        it, n, node_it = 0, len(word), self.head
        while it < n:
            index = ord(word[it]) - ord('a')
            if not node_it.letter[index]:
                node_it.letter[index] = Node() 
            node_it = node_it.letter[index] 
            it += 1
        node_it.end = True 
    def recursive_search(self, word, lp, ref):
        if (lp >= len(word)):
            return ref.end
        if (word[lp] != '.'):
            index = ord(word[lp]) - ord('a')
            if not ref.letter[index]:
                return False
            return self.recursive_search(word, lp + 1, ref.letter[index])
        else:
            for i in range(0, 26):
                if not ref.letter[i]:
                    continue 
                possibility = self.recursive_search(word, lp + 1, ref.letter[i])
                if (possibility):
                    return True
            return(False)
    def search(self, word: str) -> bool:
        ref = self.head 
        return self.recursive_search(word, 0, ref)