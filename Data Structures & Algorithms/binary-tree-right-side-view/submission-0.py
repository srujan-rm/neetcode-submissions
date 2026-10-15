# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if (not root):
            return result
        que = deque() 
        que.append(root)
        while (que):
            n = len(que) 
            for i in range(0, n):
                retrieve = que.popleft() 
                if (i == n - 1):
                    result.append(retrieve.val) 
                if (retrieve.left):
                    que.append(retrieve.left)
                if (retrieve.right):
                    que.append(retrieve.right)
        return result