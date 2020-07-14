# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        solution = []
        stack_left = []
        stack_right = []
        if root1:
            stack_left.append(root1)
        if root2:
            stack_right.append(root2)
            
        while stack_left or stack_right:
            left_value = None
            right_value = None
            left_node = None
            right_node = None
            
            if stack_left:
                cur = stack_left[-1]
                while cur.left:
                    cur_left = cur.left
                    stack_left.append(cur_left)
                    cur.left = None
                    cur = cur_left
                left_value = cur.val
                left_node = cur
                stack_left.pop()
                if cur.right:
                    stack_left.append(cur.right)
                    cur.right = None
                    
            if stack_right:
                cur = stack_right[-1]
                while cur.left:
                    cur_left = cur.left
                    stack_right.append(cur_left)
                    cur.left = None
                    cur = cur_left
                right_value = cur.val
                right_node = cur
                stack_right.pop()
                if cur.right:
                    stack_right.append(cur.right)
                    cur.right = None
                    
            
            if left_value != None and right_value == None:
                solution.append(left_value)
            elif left_value == None and right_value != None :
                solution.append(right_value)
            elif left_value > right_value:
                solution.append(right_value)
                stack_left.append(left_node)
            elif right_value > left_value:
                solution.append(left_value)
                stack_right.append(right_node)
            else:

                solution.append(left_value)
                solution.append(right_value)

        return solution
        
