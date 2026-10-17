class Node:
    def __init__(self):
        self.letter = [None for i in range(26)]
        self.end = False

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

    def search(self, word: str) -> bool:
        it, n, node_it = 0, len(word), self.head
        while it < n:
            index = ord(word[it]) - ord('a')
            if not node_it.letter[index]:
                return False
            node_it = node_it.letter[index]
            it += 1
        return(node_it.end)

    def startsWith(self, prefix: str) -> bool:
        it, n, node_it = 0, len(prefix), self.head
        while it < n:
            index = ord(prefix[it]) - ord('a')
            if not node_it.letter[index]:
                return False
            node_it = node_it.letter[index]
            it += 1 
        if (node_it):
            return True
        return False 
        