"""
199. Binary Tree Right Side View
Medium

5763

318

Add to List

Share
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
Accepted
603,077
Submissions
1,023,269
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = [root]
        res = []
        while level:
            new_level = []
            res.append(level[-1].val)
            for n in level:
                if n.left:
                    new_level.append(n.left)
                if n.right:
                    new_level.append(n.right)
            level = new_level
        return res
