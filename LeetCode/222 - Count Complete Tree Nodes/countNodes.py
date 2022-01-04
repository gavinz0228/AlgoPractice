"""
222. Count Complete Tree Nodes
Medium

4217

297

Add to List

Share
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
Accepted
368,779
Submissions
683,875
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        height = -1
        sol = None
        def count(root, curr_height, curr_count):
            if not root:
                nonlocal height
                #first height detected
                if height == -1:
                    height = curr_height
                    return False
                #first empty node who height is one less then the previous height
                elif curr_height == height - 1:
                    nonlocal sol
                    sol = curr_count - 1
                    return True
                return False
            else:
                return count(root.left, curr_height + 1, 2 * curr_count) or count(root.right, curr_height + 1, 2 * curr_count + 1)

        if(count(root, 0, 1)):
            return sol
        else:
            return 2**height - 1
                    
        
