# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        sol = 0
        def dfs(root, pre):
            nonlocal sol
            if not root:
                return
            if root.val >= pre:
                sol += 1
            cur = max(pre, root.val)
            dfs(root.left, cur)
            dfs(root.right, cur)

        dfs(root, root.val)
        return sol
