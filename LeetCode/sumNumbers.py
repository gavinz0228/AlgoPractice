# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        s = 0
        stack = [] 
        stack.append((root, 0))
        while stack:
            node, n = stack.pop()
            cur = n*10 + node.val
            if not node.left and not node.right:
                s += cur
            else:
                if node.right:
                    stack.append((node.right, cur))
                if node.left:
                    stack.append((node.left, cur))
        return s
        
