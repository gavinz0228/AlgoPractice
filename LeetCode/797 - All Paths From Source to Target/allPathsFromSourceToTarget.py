from collections import defaultdict


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        graph_dict = defaultdict(list)
        sol = []
        for n, p in enumerate(graph):
            graph_dict[n].extend(p)

        def dfs(source, desc, cur):
            cur = cur + [source]
            if source == desc:
                sol.append(cur)
            for c in graph_dict[source]:
                dfs(c, desc, cur)
        dfs(0, len(graph)-1, [])
        return sol
