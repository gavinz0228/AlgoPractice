"""
337. House Robber III
Medium

5836

89

Add to List

Share
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

Example 1:


Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:


Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 104
Accepted
271,687
Submissions
509,670
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {None: 0}
        def aux(root):
            if root in cache:
                return cache[root]

            children = 0
            grandchildren = root.val

            if root.left:
                children += aux(root.left)
                grandchildren += aux(root.left.left) + aux(root.left.right)
            if root.right:
                children += aux(root.right)
                grandchildren += aux(root.right.left) + aux(root.right.right)
            res = max(grandchildren, children)

            cache[root] = res
            return res
        return aux(root)

#solution without memerization
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def aux(root):
            if not root:
                return 0, 0
            lc, lgc = aux(root.left)
            rc, rgc = aux(root.right)
            
            return max(root.val + lgc + rgc, lc + rc), lc + rc
        
        return max(aux(root))
"""
