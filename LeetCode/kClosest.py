import heapq 
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        l = len(points)
        if K >= l:
            return points
        
        dist = [ (0- (points[x][0]**2 + points[x][1]**2) ,points[x][0], points[x][1]) for x in range(K)]
        heapq.heapify(dist)
        for i in range(K, l):
            p = points[i]
            d = 0- (p[0]**2 + p[1]**2 )    
            if d > dist[0][0]:
                heapq.heappush(dist, (d, p[0], p[1],) )
                heapq.heappop(dist)
        return [(s[1], s[2]) for s in dist]
