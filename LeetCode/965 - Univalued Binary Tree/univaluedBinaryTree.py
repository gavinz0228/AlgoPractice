# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.val = root.val
        return self.aux(root)

    def aux(self, root):
        if root.val != self.val:
            return False
        if root.left:
            res = self.aux(root.left)
            if not res:
                return res
        if root.right:
            return self.aux(root.right)
        return True
