# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.max_diff = float('inf')
        self.last = None
        self.aux(root)
        return self.max_diff
    
    def aux(self, root):
        if not root:
            return 
        self.aux(root.left)
        if self.last is not None:
            if abs(root.val - self.last.val) < self.max_diff:
                self.max_diff = abs(root.val - self.last.val)
        self.last = root
        self.aux(root.right)
        