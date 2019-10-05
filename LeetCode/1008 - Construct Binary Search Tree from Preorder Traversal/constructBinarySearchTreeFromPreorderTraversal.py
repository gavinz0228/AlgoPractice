# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        head = TreeNode(preorder[0])
        stack = [head]
        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            if preorder[i] < preorder[i - 1]:
                stack[-1].left = node
            else:
                last = stack[-1]
                while stack and preorder[i] > stack[-1].val:
                    last = stack.pop()
                last.right = node
            stack.append(node)
        return head
