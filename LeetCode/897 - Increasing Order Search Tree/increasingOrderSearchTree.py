# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        values = self.aux(root)
        head = TreeNode(values[0])
        for i in range(1, len(values)):
            curr = TreeNode(values[i])
            curr.right = head
            head = curr
        return head

    def aux(self, root):
        if not root:
            return []
        right = self.aux(root.right)
        right.append(root.val)
        right.extend(self.aux(root.left))
        return right