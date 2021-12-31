"""
449. Serialize and Deserialize BST
Medium

2426

120

Add to List

Share
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.

 

Example 1:

Input: root = [2,1,3]
Output: [2,1,3]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
0 <= Node.val <= 104
The input tree is guaranteed to be a binary search tree.
Accepted
178,262
Submissions
320,533
"""


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        result = []
        if root:
            def compress(node):
                if node:
                    result.append(str(node.val))
                    compress(node.left)
                    compress(node.right)
                else:
                    result.append('N')
            compress(root)                    
            return " ".join(result)
        else:
            return ''
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None

        num_strs = data.split(" ")
        length = len(num_strs)

        def decompress(i):
            if num_strs[i] != 'N':
                node = TreeNode(int(num_strs[i]))
                node.left, new_i = decompress(i+1)
                node.right, new_i = decompress(new_i)
                return node, new_i
            else:
                return None, i + 1
        head, _ = decompress(0)
        return head
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
"""
