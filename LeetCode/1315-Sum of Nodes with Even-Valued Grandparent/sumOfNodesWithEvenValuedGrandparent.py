# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sol = 0
        mem_dict = {}
        def dfs(root, lvl, mem):
            if not root:
                return
            nonlocal sol
            if lvl > 1:
                if mem[lvl-2] % 2 == 0:
                    sol += root.val

            mem[lvl] = root.val
            
            dfs(root.left, lvl+1, mem)
            dfs(root.right, lvl+1, mem)
            
        dfs(root, 0,mem_dict)
        return sol
