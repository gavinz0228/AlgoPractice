"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root])
        while q:
            front = q[0]
            last = None
            while q:
                cur = q.pop()
                if last:
                    last.next = cur
                last = cur
                if cur.left:
                    q.appendleft(cur.left)
                if cur.right:
                    q.appendleft(cur.right)
                if cur == front:
                    break
        return root
