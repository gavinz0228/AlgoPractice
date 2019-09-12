# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
class Solution:
    def postorderTraversal(self, root: 'TreeNode') -> List[int]:
        if not root:
            return root
        result = []
        stack = [root]
        while stack:
            n = stack[-1]
            if not n.left and not n.right:
                stack.pop()
                result.append(n.val)
            else:
                if n.right:
                    stack.append(n.right)
                    n.right = None
                    #print(stack)
                if n.left:
                    stack.append(n.left)
                    n.left = None

        return result
"""
#Solution using set to remember visited node
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return root
        result = []
        stack = [root]
        added = set([None])
        while stack:

            n = stack[-1]
            if n.left in added and n.right in added:
                stack.pop()
                result.append(n.val)
            else:
                if n.right and n.right not in added:
                    stack.append(n.right)
                    added.add(n.right)
                    #print(stack)
                if n.left  and n.left not in added:
                    stack.append(n.left)
                    added.add(n.left)

        return result
            
"""