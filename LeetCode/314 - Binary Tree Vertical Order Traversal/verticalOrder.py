'''
314. Binary Tree Vertical Order Traversal
Medium

1504

198

Add to List

Share
Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Example 2:


Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]
Example 3:


Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
Output: [[4],[9,5],[3,0,1],[8,2],[7]]
Example 4:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
Accepted
166,334
Submissions
349,356
'''
from collections import defaultdict
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(root, 0)]
        left = 0
        right = 0
        res = defaultdict(list)
        while queue:
            _queue = []
            for node, idx in queue:
                if idx < left:
                    left = idx
                elif idx > right:
                    right = idx

                res[idx].append(node.val)
                    
                if node.left:
                    _queue.append((node.left, idx -1))
                if node.right:
                    _queue.append((node.right, idx +1))
            queue = _queue
        return [ res[i] for i in range(left, right + 1)]
    
