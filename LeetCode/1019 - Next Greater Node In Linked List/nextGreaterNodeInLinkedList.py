# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from collections import deque
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        if not nums:
            return []
        stack = [nums[-1]]
        result = deque([0])
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < stack[-1]:
                result.appendleft(stack[-1])
            else:
                last = stack.pop()
                while last <= nums[i] and stack:
                    last = stack.pop()
                if last <= nums[i]:
                    result.appendleft(0)
                else:
                    stack.append(last)
                    result.appendleft(last)
            stack.append(nums[i])
        return result