# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.sol = []
        self.sum = sum
        if not root.left and not root.right:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        self.backtrack(root, [], 0)
        return self.sol
    
    def backtrack(self, root, curr, count):
        if not root.left and not root.right:
            if count + root.val == self.sum:
                self.sol.append(curr + [root.val])
        curr.append(root.val)
        count += root.val
        if root.left:
            self.backtrack(root.left, curr, count)
        if root.right:
            self.backtrack(root.right, curr, count)
        curr.pop()
        count -= root.val