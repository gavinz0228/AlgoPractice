"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        lookup = {}
        if not node:
            return node
        def clone(node):
            if node.val not in lookup:
                children = []
                new_node = Node(node.val, children)
                lookup[node.val] = new_node
                for nei in node.neighbors:
                    if nei.val not in lookup:
                        clone(nei)
                    children.append(lookup[nei.val])
        clone(node)
        return lookup[node.val]