# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        level = 1
        if d == 1:
            n = TreeNode(v)
            n.left = root
            return n
        head = root
        q = deque([root])
        while q:
            if level == d - 1:
                newq = deque()
                while q:
                    cur = q.pop()
                    savedLeft = cur.left
                    savedRight = cur.right
                    cur.left = TreeNode(v)
                    cur.right = TreeNode(v)
                    if savedLeft:
                        cur.left.left = savedLeft
                    if savedRight:
                        cur.right.right = savedRight
                break
            else:
                newq = deque()
                while q:
                    cur = q.pop()
                    if cur.left:
                        newq.append(cur.left)
                    if cur.right:
                        newq.append(cur.right)
                q = newq 
            level += 1
        return head
