"""
95. Unique Binary Search Trees II
Medium

4296

282

Add to List

Share
Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique values from 1 to n. Return the answer in any order.

 

Example 1:


Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 8
Accepted
286,220
Submissions
594,379
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        nums = range(n)
        def generate(low, high):
            if low == high:
                return [None]
            res = []
            for i in range(low, high):
                
                left_trees = generate(low, i)
                right_trees = generate(i + 1, high)
                for l in left_trees:
                    for r in right_trees:
                        mid = TreeNode(nums[i] + 1)
                        mid.left = l
                        mid.right = r
                        res.append(mid)
            return res
        return generate(0, n)
        
