# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        def aux(root, toAdd):
            if not root:
                return 0
            rsum = aux(root.right, toAdd)
            lsum = aux(root.left, toAdd + rsum + root.val)
            cur = root.val
            root.val += rsum + toAdd
            return cur + lsum + rsum
        aux(root, 0)
        return root