'''
236. Lowest Common Ancestor of a Binary Tree
Medium

5942

208

Add to List

Share
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [1,2], p = 1, q = 2
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the tree.
Accepted
666,579
Submissions
1,329,795
'''
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        _,_,res = self.find(root, p, q)
        return res
    def find(self, root, p, q):
        if not root:
            return False, False, None
        lp,lq,lf = self.find(root.left, p, q)
        if lf:
            return True, True, lf
        rp,rq,rf = self.find(root.right, p, q)
        if rf:
            return True, True, rf
        if (lp or rp) and (lq or rq):
            return True, True, root
        elif (lp or rp) and q == root:
            return True, True, root
        elif (lq or rq) and p == root:
            return True, True, root
        else:
            cp = p == root
            cq = q == root
            return lp or rp or cp, lq or rq or cq, None
