# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.sol = []
        to_delete = set(to_delete)
        if root.val not in to_delete:
            self.sol.append(root)
        self.aux(root, to_delete)
        return self.sol

    def aux(self, root, to_delete):
        if not root:
            return False
        found = self.aux(root.left, to_delete)
        if found:
            root.left = None
        found = self.aux(root.right, to_delete)
        if found:
            root.right = None
        if root.val in to_delete:
            if root.left:
                self.sol.append(root.left)
            if root.right:
                self.sol.append(root.right)
            root.left, root.right = None, None
            return True
        return False
