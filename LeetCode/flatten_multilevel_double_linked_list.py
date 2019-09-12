"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head
        self.aux(head);
        return head
    def aux(self, head):
        curr = head
        last = curr
        while curr:
            if curr.child:
                nxt = curr.next
                last_node = self.aux(curr.child)
                curr.next = curr.child
                curr.child.prev = curr
                last_node.next = nxt
                if nxt:
                    nxt.prev = last_node
                curr.child = None
                last = last_node
                curr = nxt
            else:
                last = curr
                curr = curr.next    
        return last
                
