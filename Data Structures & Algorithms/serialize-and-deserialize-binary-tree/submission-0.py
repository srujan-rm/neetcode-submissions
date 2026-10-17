# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    def __init__(self):
        self.serialization_arr = []
        self.ptr = 0
    def initialize(self, root):
        if not root:
            self.serialization_arr.append(".")
            return
        self.serialization_arr.append(str(root.val) + ",")
        self.initialize(root.left)
        self.initialize(root.right) 
        return
    def create(self, data):
        if (data[self.ptr] == '.'):
            self.ptr += 1
            return None 
        digit = []
        while (self.ptr < len(data) and data[self.ptr].isdigit()):
            digit.append(data[self.ptr])
            self.ptr += 1
        num = int("".join(digit))
        node = TreeNode(num)
        self.ptr += 1
        node.left = self.create(data)
        node.right = self.create(data) 
        return node
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.initialize(root)
        return "".join(self.serialization_arr)
    def deserialize(self, data: str) -> Optional[TreeNode]:
        return(self.create(data)) 