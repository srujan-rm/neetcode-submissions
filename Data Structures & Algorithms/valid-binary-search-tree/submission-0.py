# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verify(self, root, min_value=float("-inf"), max_value=float("inf")):
        if not root:
            return True
        if (root.val > min_value and root.val < max_value):
            return self.verify(root.left, min_value, root.val) and self.verify(root.right, root.val, max_value)
        else:
            return False
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return if the tree is a valid BST or not
        return(self.verify(root)) 