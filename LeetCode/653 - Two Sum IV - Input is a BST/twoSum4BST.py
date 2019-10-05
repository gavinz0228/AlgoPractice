# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.k = k
        self.visited = set([])
        self.res = False
        self.traverse(root)
        return self.res

    def traverse(self, root):
        if not root:
            return
        if self.k - root.val in self.visited:
            self.res = True
            return
        self.visited.add(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

        