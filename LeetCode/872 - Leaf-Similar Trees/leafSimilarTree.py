# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: 'TreeNode', root2: 'TreeNode') -> bool:
        leaves1 = [] 
        leaves2 = []
        self.getLeaves(root1, leaves1)
        self.getLeaves(root2, leaves2)
        l1 = len(leaves1)
        l2 = len(leaves2)
        if l1 != l2:
            return False
        return all([ leaves1[i] == leaves2[i] for i in range(l1)])
    def getLeaves(self, root, leaves):
        if not root.left and not root.right:
            leaves.append(root.val)
        if root.left:
            self.getLeaves(root.left, leaves)
        if root.right:
            self.getLeaves(root.right, leaves)