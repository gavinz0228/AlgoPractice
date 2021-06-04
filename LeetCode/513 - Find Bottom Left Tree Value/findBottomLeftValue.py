'''
513. Find Bottom Left Tree Value
Medium

1401

175

Add to List

Share
Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:


Input: root = [2,1,3]
Output: 1
Example 2:


Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
Accepted
134,221
Submissions
212,658
'''
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return None
        q = [root]
        last_row = None
        while q:
            _q = []
            for n in q:
                if n.left:
                    _q.append(n.left)
                if n.right:
                    _q.append(n.right)
                    
            last_row = q
            q = _q
        return last_row[0].val
