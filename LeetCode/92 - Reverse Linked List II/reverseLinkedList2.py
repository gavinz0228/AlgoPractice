# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseBetween(self, head: 'ListNode', m: int, n: int) -> 'ListNode':
        if m == n:
            return head
        before = None
        after = None
        cur = head
        i = 1
        prev = None
        while cur:
            nxt = cur.next
            if i >= m and i <= n:
                if i == m:
                    rev_tail = cur
                    prev = rev_tail
                elif i == n:
                    rev_head = cur
                    cur.next = prev
                else:
                    cur.next = prev
                    prev = cur
            elif i == m - 1:
                before = cur
            elif i == n + 1:
                after = cur
            cur = nxt
            i += 1
        new_head = head
        if not before:
            new_head = rev_head
        else:
            before.next = rev_head
        rev_tail.next = after
        return new_head
