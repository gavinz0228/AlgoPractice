"""
143. Reorder List
Medium

5169

198

Add to List

Share
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
Accepted
433,135
Submissions
933,617
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
        l = len(nodes)
        if l == 1:
            return head
        last = None
        for i in range(int(l / 2)):
            nodes[i].next = nodes[l - i - 1]
            if last:
                last.next = nodes[i]
            last = nodes[i].next
        if l % 2 == 1:
            last.next = nodes[int(l/2)]
            last.next.next = None
        else:
            last.next = None
        return nodes[0]
