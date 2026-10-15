# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [] 
        if not root:
            return result
        
        que = deque()
        que.append(root) 
        while (que):
            n = len(que)
            sublist = []
            for i in range(0, n):
                retrieve = que.popleft() 
                sublist.append(retrieve.val) 
                if (retrieve.left):
                    que.append(retrieve.left)
                if (retrieve.right):
                    que.append(retrieve.right)
            result.append(sublist)
        return result