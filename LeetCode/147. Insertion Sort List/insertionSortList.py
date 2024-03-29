"""
147. Insertion Sort List
Medium

1828

780

Add to List

Share
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.


 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
 

Constraints:

The number of nodes in the list is in the range [1, 5000].
-5000 <= Node.val <= 5000
Accepted
274,069
Submissions
568,112
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def insertNode(head, node):
            curr = head
            prev = None
            while curr:
                if node.val < curr.val:
                    if prev:
                        temp = prev.next
                        prev.next = node
                        node.next = temp
                        return head
                    else:
                        node.next = head
                        return node
                prev = curr
                curr = curr.next
            
            if not head:
                node.next = None
                return node
            else:
                prev.next = node
                node.next = None
                return head
                
        new_head = None
        curr = head
        while curr:
            nxt = curr.next
            new_head = insertNode(new_head, curr)
            curr = nxt
        return new_head
