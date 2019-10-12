# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        cur = head.next
        pre = head
        while cur:
            while cur and cur.val == val:
                cur = cur.next
                pre.next = cur

            pre = cur
            if cur:
                cur = cur.next
            else:
                break
        return head
