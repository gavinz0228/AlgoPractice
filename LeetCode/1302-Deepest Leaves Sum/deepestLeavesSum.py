# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        maxl = 0
        mem = {}

        def dfs(root, lvl):
            if not root:
                return
            nonlocal maxl
            if lvl < maxl:
                pass
            elif lvl == maxl:
                mem[lvl] += root.val
            else:
                mem[lvl] = root.val
                maxl = lvl
            dfs(root.left, lvl+1)
            dfs(root.right, lvl+1)
            
        dfs(root, 1)
        return mem[maxl]
                
