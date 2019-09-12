# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
class Solution:
    def mergeTrees(self, t1, t2):
        res = t1
        if not t1 and not t2:
            return None
        elif not t1 and t2:
            return t2
        elif t1 and not t2:
            return t1
        else:
            res.val += t2.val
            self.aux(t1, t2)
        return res
    def aux(self, t1, t2 ):

        if t1.left and t2.left:
            t1.left.val += t2.left.val
            self.aux(t1.left, t2.left)
        elif not t1.left and t2.left:
            t1.left = t2.left
            
        if t1.right and t2.right:
            t1.right.val += t2.right.val
            self.aux(t1.right, t2.right)
        elif not t1.right and t2.right:
            t1.right = t2.right
        
        