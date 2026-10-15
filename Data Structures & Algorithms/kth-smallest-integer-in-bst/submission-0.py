# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.counting = 0
        self.result = None
        self.k = None
    def inorder(self, root):
        if not root:
            return False
        check = self.inorder(root.left)
        if (check == True):
            return True 
        else:
            self.result = root.val 
            self.counting += 1
            if (self.counting == self.k):
                return True
            check = self.inorder(root.right) 
            if (check):
                return True
            else:
                return False
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # in a BINARY SEARCH TREE, RETURN THE KTH SMALLEST INTEGER
        self.k = k
        self.inorder(root) 
        return self.result