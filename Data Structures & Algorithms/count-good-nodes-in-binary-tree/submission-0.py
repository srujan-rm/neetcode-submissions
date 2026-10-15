# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.root_val = None
        self.counting = 0
    def count(self, root, greatest_from_root):
        if not root:
            return
        if (root.val >= greatest_from_root):
            self.counting += 1 
        self.count(root.left, max(greatest_from_root, root.val))
        self.count(root.right, max(greatest_from_root, root.val))
    def goodNodes(self, root: TreeNode) -> int:
        self.root_val = root.val 
        greatest_from_root = float("-inf")
        self.count(root, greatest_from_root)
        return self.counting