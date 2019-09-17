# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        if not root:
            return [0]
        q = deque([root])
        while q:
            last = q[0]
            seen_last = False
            nums = []
            while q:
                node = q.pop()

                if node == last:
                    seen_last = True
                nums.append(node.val)
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
                if seen_last:
                    break
            res.append(sum(nums) / len(nums))
        return res
