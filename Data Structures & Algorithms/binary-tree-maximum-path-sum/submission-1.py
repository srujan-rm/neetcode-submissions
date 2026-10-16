class Solution:
    def __init__(self):
        self.maximal = float("-inf")
    def pathFromNode(self, root):
        if not root:
            return 0
        evaluateLeft = self.pathFromNode(root.left)
        evaluateRight = self.pathFromNode(root.right)
        self.maximal = max(self.maximal, evaluateLeft + root.val, evaluateRight + root.val, root.val, evaluateLeft + root.val + evaluateRight)
        return max(evaluateLeft + root.val, evaluateRight + root.val, root.val)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        resultant = self.pathFromNode(root)
        self.maximal = max(self.maximal, resultant)
        return self.maximal