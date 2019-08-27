# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.sol = - float('inf')
        lookup = {root.val:1}
        self.aux(root, lookup)
        return self.sol
    def aux(self, root, lookup):
        if not root:
            return
        for k,v in lookup.items():
            if abs(k - root.val) > self.sol:
                self.sol = abs(k - root.val)
                
        lookup[root.val] = lookup.get(root.val, 0) + 1
        self.aux(root.left, lookup)
        self.aux(root.right, lookup)
        if lookup[root.val] == 1:
            del lookup[root.val]
        else:
            lookup[root.val] -= 1