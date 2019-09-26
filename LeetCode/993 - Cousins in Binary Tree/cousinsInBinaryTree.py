# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = []
        if root.left:
            q.append(root.left)
        if root.right:
            q.append(root.right)
        while len(q) > 0:
            new_q = []
            parent = []
            for n in q:
                if n.left:
                    if n.left.val == x or n.left.val == y:
                        parent.append(n)
                    new_q.append(n.left)
                if n.right:
                    if n.right.val == x or n.right.val == y:
                        parent.append(n)
                    new_q.append(n.right)
            if parent:
                if len(parent) == 1:
                    return False
                return parent[0] != parent[1]
            q = new_q
        return False
