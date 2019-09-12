# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkNode(self, left, right):
        if not left and not right:
            return True
        elif (not left and right) or (left and not right):
            return False
        else:
            if left.val == right.val:
                return True
            else:
                return False
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not self.checkNode(root.left, root.right):
            return False
        if not root.left:
            return True
        return self.aux(root.left, root.right)
        
    def aux(self, left, right):
        if not self.checkNode(left, right):
            return False
        if left:
            if not self.aux( left.left, right.right):
                return False
            if not self.aux(left.right, right.left):
                return False
        return True
#Traver the tree with two stacks
"""
class Solution:
    def checkNode(self, left, right):
        if not left and not right:
            return True
        elif (not left and right) or (left and not right):
            return False
        else:
            if left.val == right.val:
                return True
            else:
                return False
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        if not self.checkNode(root.left, root.right):
            return False
        if not root.left:
            return True
        
        ls = [root.left]
        rs = [root.right]
        while ls:
            ln = ls.pop()
            rn = rs.pop()
            if not self.checkNode(ln.left, rn.right):
                return False
            if ln.left:
                ls.append(ln.left)
                rs.append(rn.right)
            if not self.checkNode(ln.right, rn.left):
                return False
            if ln.right:
                ls.append(ln.right)
                rs.append(rn.left)
        return True
"""
