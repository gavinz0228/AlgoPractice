"""
501. Find Mode in Binary Search Tree
Easy

1893

518

Add to List

Share
Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [1,null,2,2]
Output: [2]
Example 2:

Input: root = [0]
Output: [0]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
 

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
Accepted
138,797
Submissions
298,964
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = 0
        max_count = 0
        sol = set([])
        last = None
        def traverse(root):

            if not root:
                return
            nonlocal sol
            nonlocal last
            nonlocal count
            nonlocal max_count

            traverse(root.left)
            
            if last == root.val:
                count += 1
            else:
                if count > max_count:
                    sol = set([last])
                    max_count = count
                elif count == max_count:
                    sol.add(last)
                count = 1
            last = root.val
            traverse(root.right)
        traverse(root)

        if count > max_count:
            sol = [last]
        elif count == max_count:
            sol.add(last)
        
        return sol
