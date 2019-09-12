# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        self.last = None
        self.aux(root)
    def aux(self, root):
        if self.last:
            self.last.left = None
            self.last.right = root
        left_backup = root.left
        right_backup = root.right
        self.last = root
        if root.left:
            self.aux(root.left)
        if right_backup:
            self.aux(right_backup)
