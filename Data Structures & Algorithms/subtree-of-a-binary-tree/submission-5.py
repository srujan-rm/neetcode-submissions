# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def serialize(self, root, arr):
        if (not root):
            arr.append(".")
            return
        self.serialize(root.left, arr)
        self.serialize(root.right, arr)
        arr.append(str(root.val))
        return

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_str, subroot_str = [], []
        self.serialize(root, root_str)
        self.serialize(subRoot, subroot_str)
        root_str = ",".join(root_str)
        subroot_str = ",".join(subroot_str)
        if (root_str.find(subroot_str) != -1):
            return True
        else:
            return False
