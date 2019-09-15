# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head 
        while True:
            if not fast.next:
                return slow
            if not fast.next.next:
                return slow.next
            slow = slow.next
            fast = fast.next.next