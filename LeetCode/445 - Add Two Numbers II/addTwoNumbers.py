'''
445. Add Two Numbers II
Medium

2434

201

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [7,2,4,3], l2 = [5,6,4]
Output: [7,8,0,7]
Example 2:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [8,0,7]
Example 3:

Input: l1 = [0], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
 

Follow up: Could you solve it without reversing the input lists?

Accepted
243,890
Submissions
428,726
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        carry = 0
        last = None
        head = None
        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            val = (n1 + n2 + carry)
            rem = val % 10
            carry = int(val / 10)
            head = ListNode(rem)
            head.next = last
            last = head
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        if carry == 1:
            head = ListNode(carry)
            head.next = last
        return head
    def reverse(self, head):
        last = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = last
            last = curr
            curr = tmp
        return last
    
