"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from typing import List
from collections import deque


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        result = deque([])
        while stack:
            node = stack.pop()
            result.appendleft(node.val)
            for c in node.children:
                stack.append(c)
        return result
