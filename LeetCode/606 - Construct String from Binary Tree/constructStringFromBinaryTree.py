# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        sol = []
        if not t:
            return ""
        def concat(t):
            if not t:
                return
            sol.append(str(t.val))
            if t.left or t.right:
                sol.append("(")
                concat(t.left)
                sol.append(")")
            if t.right:
                sol.append("(")
                concat(t.right)
                sol.append(")")
        concat(t)
        return "".join(sol)
            
        