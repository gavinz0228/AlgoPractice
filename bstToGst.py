# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.s = 0
        newRoot = self.aux(root)
        return newRoot
    def aux(self, root):
        if not root:
            return None
        rn = self.aux(root.right)
        self.s += root.val
        newRoot = TreeNode(self.s)
        ln= self.aux(root.left) 
        
        newRoot.left = ln
        newRoot.right = rn
        return newRoot
        
