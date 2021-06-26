'''
102. Binary Tree Level Order Traversal
Medium

5092

111

Add to List

Share
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
Accepted
887,494
Submissions
1,531,810
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        que = deque([root])
        ans = []

        while que:
            level = []
            for _ in range(len(que)):
                curr = que.pop()
                level.append(curr.val)
                if curr.left:
                    que.appendleft(curr.left)
                if curr.right:
                    que.appendleft(curr.right)
            ans.append(level)
        return ans


