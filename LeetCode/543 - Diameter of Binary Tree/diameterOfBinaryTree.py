# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: 'TreeNode') -> int:
        if not root:
            return 0
        self.length = 0
        self.aux(root)
        return self.length
    def aux(self, root):
        if not root:
            return 0
        left = self.aux(root.left)
        right = self.aux(root.right)
        if left + right >= self.length:
            self.length = left + right
        return max(left, right) + 1