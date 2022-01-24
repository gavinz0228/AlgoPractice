"""
82. Remove Duplicates from Sorted List II
Medium

4279

144

Add to List

Share
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
Accepted
408,699
Submissions
971,579
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        new_head = None
        last = curr
        last_valid_node = None
        if not curr or not curr.next:
            return head
        
        curr = curr.next
        count = 1
        while curr:
            if curr.val != last.val:
                if count == 1:
                    #taking it
                    last.next = None
                    if not new_head:
                        new_head = last
                        last_valid_node = last
                    else:
                        last_valid_node.next = last
                        last_valid_node = last_valid_node.next
                count = 1
            else:
                count += 1
            
            last = curr
            curr = curr.next
        if count == 1:
            if not last_valid_node:
                return last
            else:
                last_valid_node.next = last
                last_valid_node.next.next = None
        return new_head
