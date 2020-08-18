# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        sol = 0
        def isPseudoPalindrome(nums):
            count_dict = Counter(nums)
            odd_count = 0
            for v in count_dict.values():
                if v % 2 == 1:
                    odd_count += 1
            if odd_count > 1:
                return False
            else:
                return True
        def dfs(root, curr):
            curr.append(root.val)
            if root.left or root.right:
                if root.left:
                    dfs(root.left, curr)
                if root.right:
                    dfs(root.right, curr)
                
            else:
                if isPseudoPalindrome(curr):
                    nonlocal sol
                    sol += 1
            curr.pop()
        if root:
            dfs(root, [])
            return sol
        else:
            return 0
        
