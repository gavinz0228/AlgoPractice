from collections import defaultdict


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.graph = defaultdict(set)
        for s, d in edges:
            self.visited = set()
            if s in self.graph and d in self.graph and self.search(s, d):
                return (s, d)
            self.graph[s].add(d)
            self.graph[d].add(s)
        return False

    def search(self, s, d):
        if s not in self.visited:
            self.visited.add(s)
            if s == d:
                return True
            for neigh in self.graph[s]:
                if self.search(neigh, d):
                    return True
            return False
