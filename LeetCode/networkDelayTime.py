from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = {}
        best_time = {}
        
        for t in times:
            if t[0] not in graph:
                graph[t[0]] = []
            graph[t[0]].append( (t[1], t[2],) )
        if K not in graph:
            return -1
        #dfs
        dq = deque([(K, 0)])
        
        while dq:
            n, cur_time = dq.pop()
            if n not in best_time:
                best_time[n] = cur_time
            else:
                if cur_time < best_time[n]:
                    best_time[n] = cur_time
                else:
                    continue
            if n not in graph:
                continue
            for target, time in graph[n]:
                dq.appendleft( (target,cur_time + time) )      
        if len(best_time) != N:
            return -1
        else:
            return max(best_time.values())
