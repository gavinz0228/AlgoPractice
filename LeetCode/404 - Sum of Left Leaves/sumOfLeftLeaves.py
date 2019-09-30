# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sol = 0
        if not root:
            return 0
        self.aux(root, False)
        return self.sol

    def aux(self, root, is_left):
        if not root.left and not root.right:
            if is_left:
                self.sol += root.val
        else:
            if root.left:
                self.aux(root.left, True)
            if root.right:
                self.aux(root.right, False)
