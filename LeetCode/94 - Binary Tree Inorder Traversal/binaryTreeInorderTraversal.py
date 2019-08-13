# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sol = []
        if not root:
            return
        stack = [root]
        while stack:
            cur = stack[-1]
            if not cur.left:
                sol.append(cur.val)
                stack.pop()
                if cur.right:
                    stack.append(cur.right)
                    #cur.right = None
                
            else:
                stack.append(cur.left)
                cur.left = None
    
        return sol