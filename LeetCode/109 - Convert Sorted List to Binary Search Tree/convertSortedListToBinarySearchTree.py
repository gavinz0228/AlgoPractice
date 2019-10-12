# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return self.make(arr, 0, len(arr))
        
    def make(self, arr, start, end):
        if end == start:
            return None
        elif end - start == 1:
            return TreeNode(arr[start])
        mid  = int((end + start) / 2)
        root = TreeNode(arr[mid])
        root.left = self.make(arr, start, mid)
        root.right = self.make(arr, mid + 1, end)
        return root
