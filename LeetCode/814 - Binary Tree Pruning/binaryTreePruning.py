# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        self.aux(root)
        return root

    def aux(self, root):
        if not root:
            return True
        left_zero = self.aux(root.left)
        right_zero = self.aux(root.right)
        if left_zero and right_zero and root.val == 0:
            return True
        if left_zero:
            root.left = None
        if right_zero:
            root.right = None
