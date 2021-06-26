'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

5776

142

Add to List

Share
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.
Accepted
533,822
Submissions
990,243
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#preorder : root, left, right
#inorder : left, root, right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        inor_map = {n: i for i,n in enumerate(inorder)}
        pre_id = 0
        def helper(in_start, in_end):
            nonlocal pre_id
            if pre_id >= len(preorder) or in_start > in_end:
                return None
            root_val = preorder[pre_id]
            pre_id += 1
            in_id = inor_map[root_val]
            if in_id < in_start:
                return None
            root = TreeNode(root_val)
            root.left = helper(in_start, in_id - 1)
            root.right = helper(in_id + 1, in_end)
            return root
        return helper(0, len(inorder) - 1)