# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.sol = None
        self.k = k
        self.idx = 0
        self.aux(root)
        return self.sol
    def aux(self, root):
        if not root:
            return
        if not self.sol:
            self.aux(root.left)
        if not self.sol:
            self.idx += 1
            if self.idx == self.k:
                self.sol = root.val
        if not self.sol:
            self.aux(root.right)
