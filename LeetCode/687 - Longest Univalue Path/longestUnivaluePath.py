# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        max_num = 1
        if not root:
            return 0

        def count(root):
            nonlocal max_num
            if not root:
                return None, 0
            lastl, numl = count(root.left)
            lastr, numr = count(root.right)
            if lastl == lastr and lastl == root.val:
                cur = numl + numr + 1
                if cur > max_num:
                    max_num = cur
                return root.val, max(numl, numr) + 1
            elif lastl == root.val:
                cur = numl + 1
                if cur > max_num:
                    max_num = cur
                return root.val, cur
            elif lastr == root.val:
                cur = numr + 1
                if cur > max_num:
                    max_num = cur
                return root.val, cur
            else:
                return root.val, 1

        count(root)
        return max_num - 1
