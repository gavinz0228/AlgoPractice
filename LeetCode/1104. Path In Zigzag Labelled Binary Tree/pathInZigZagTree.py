"""
1104. Path In Zigzag Labelled Binary Tree
Medium

904

251

Add to List

Share
In an infinite binary tree where every node has two children, the nodes are labelled in row order.

In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.



Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

 

Example 1:

Input: label = 14
Output: [1,3,4,14]
Example 2:

Input: label = 26
Output: [1,2,6,10,26]
 

Constraints:

1 <= label <= 10^6
Accepted
30,908
Submissions
41,636
"""
import math
from collections import deque
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        bin_tree = []
        l = 2
        n = 0
        direction = 1
        label_id = 0
        while l/2 <= label:
            idx = range(int(l/2), l) if direction == 1 else  range(l-1, int(l/2)-1, -1)
            for i in idx:
                bin_tree.append(i)
                if i == label:
                    label_id = len(bin_tree) - 1
            l *= 2
            direction *= -1
        res = deque([])
        while label_id != 0:
            res.appendleft(bin_tree[label_id])
            label_id = int((label_id - 1)/2)
        res.appendleft(1)
        return res
