# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: 'TreeNode') -> int:
        self.all_sum = []
        self.aux(root, 1)
        maxs = max(self.all_sum)
        for i, s in enumerate(self.all_sum):
            if s == maxs:
                return i + 1
            
    def aux(self, root, level):
        if not root:
            return
        if len(self.all_sum) < level:
            self.all_sum.append(root.val)
        else:
            self.all_sum[level - 1] += root.val
        self.aux(root.left, level + 1)
        self.aux(root.right, level + 1)
        