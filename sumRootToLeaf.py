class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sol = [0]
        if not root:
            return 0
        self.aux( root, 0, sol)
        return sol[0]
    def aux(self, root, curr, sol):
        curr = (curr << 1) + root.val 
        if root.left:
            self.aux(root.left, curr, sol)
        if root.right:
            self.aux(root.right, curr, sol)
        if not root.left and not root.right:
            sol[0] = sol[0] + curr
