# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root):
        if not root:
            return (True, 0)


        isBalanced_l, leftDepth = self.maxDepth(root.left)
        if (not isBalanced_l):
            return (False, -1)

        isBalanced_r, rightDepth = self.maxDepth(root.right)
        if (not isBalanced_r):
            return (False, -1)
        
        if abs(leftDepth - rightDepth) > 1:
            return (False, -1)
        
        return (True, max(leftDepth, rightDepth) + 1)  

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        resultant, _ = self.maxDepth(root) 
        return resultant