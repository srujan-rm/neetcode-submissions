# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.hashmap = dict()
    def construct(self, preorder, inorder, pre_lp, pre_rp, in_lp, in_rp):
        if (pre_lp > pre_rp) or (in_lp > in_rp):
            return None
        node = TreeNode(preorder[pre_lp])
        num_elements = self.hashmap[pre_lp] - in_lp 
        node.left = self.construct(preorder, inorder, pre_lp + 1, pre_lp + num_elements, in_lp, self.hashmap[pre_lp] - 1)
        node.right = self.construct(preorder, inorder, pre_lp + num_elements + 1, pre_rp, self.hashmap[pre_lp] + 1, in_rp)
        return node
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hashmap where, you put preorder index, you got inorder index
        elementToPost = dict()
        for i in preorder:
            elementToPost[i] = None
        for i in range(0, len(inorder)):
            if inorder[i] in elementToPost:
                elementToPost[inorder[i]] = i
        for i in range(0, len(preorder)):
            if preorder[i] in elementToPost:
                self.hashmap[i] = elementToPost[preorder[i]] 
        return self.construct(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)