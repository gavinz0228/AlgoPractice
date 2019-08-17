# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left:
            lmin, lmax, valid = self.aux(root.left)
            if not valid or lmax >= root.val:
                return False
        if root.right:
            rmin, rmax, valid = self.aux(root.right)
            if not valid or rmin <= root.val:
                return False
        return True

    def aux(self, root):
        lmin = None
        rmax = None
        if root.left:
            lmin, lmax, valid = self.aux(root.left)
            if not valid or lmax >= root.val:
                return None, None, False
        if root.right:
            rmin, rmax, valid = self.aux(root.right)
            if not valid or rmin <= root.val:
                return None, None, False
        if not lmin:
            lmin = root.val
        if not rmax:
            rmax = root.val
        return lmin, rmax, True