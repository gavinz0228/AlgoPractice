# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack  = []
        if root:
            if root.right:
                self.stack.append(root.right)
            self.stack.append(root.val)
            if root.left:
                self.stack.append(root.left)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if self.stack:
            if isinstance(self.stack[-1], int): 
                return self.stack.pop()
            else:
                while self.stack:
                    ele = self.stack.pop()
                    if isinstance(ele, int): 
                        return ele
                    if ele.right:
                        self.stack.append(ele.right)
                    if not ele.left:  
                        return ele.val
                    else:
                        self.stack.append(ele.val)
                        self.stack.append(ele.left)

                

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if not self.stack:
            return False
        else:
            return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
