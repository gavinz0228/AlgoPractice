# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.mins = []
        self.aux(root)
        if len(self.mins) >=2:
            return self.mins[1]
        else:
            return -1
    def aux(self, root):
        if not root:
            return
        if not self.mins:
            self.mins.append(root.val)
        elif root.val not in self.mins:
            if len(self.mins) == 1:
                self.mins.append(root.val)
                self.mins.sort()
            else:
                self.mins.append(root.val)
                self.mins.sort()
                self.mins.pop()
        self.aux(root.left)
        self.aux(root.right)
            