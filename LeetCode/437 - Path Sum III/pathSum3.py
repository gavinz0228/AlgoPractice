# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.sum = sum
        self.count = 0
        self.aux(root, {})
        return self.count
    def aux(self, root, ht):
        print("start", ht)
        if not root:
            return
        if self.sum - root.val in ht :
            self.count += ht[self.sum - root.val]

        if self.sum == root.val:
            if root.val in ht:
                ht[root.val] += 1
                #print(ht)
                self.count += ht[root.val]
            else:
                self.count += 1
                ht[root.val] = 1

        lht = { k+root.val:v for k,v in ht.items()}
        if root.val not in lht:
            lht[root.val] = 1
        else:
            lht[root.val] += 1
        rht = { k+root.val:v for k,v in ht.items()}
        if root.val not in rht:
            rht[root.val] = 1
        else:
            rht[root.val] += 1
        self.aux(root.left, lht)
        self.aux(root.right, rht)
        print("end", ht)
print()