class Solution:
    def __init__(self):
        self.diameter_count = 0
    def maxDepth(self, root):
        if not root:
            return 0
        check_left = self.maxDepth(root.left)
        check_right = self.maxDepth(root.right)
        possible_diameter = check_left + check_right
        self.diameter_count = max(self.diameter_count, possible_diameter)
        return max(check_left, check_right) + 1 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDepth(root) 
        return self.diameter_count