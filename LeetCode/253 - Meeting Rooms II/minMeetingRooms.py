'''
253. Meeting Rooms II
Medium

3874

65

Add to List

Share
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1
 

Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106
Accepted
435,542
Submissions
917,510
'''

import heapq
class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        sol = 1
        intervals.sort()
        heap = [intervals[0][1]]
        for i in range(1, len(intervals)):
            if heap[0] <= intervals[i][0]:
                heapq.heappop(heap)
            heapq.heappush(heap, intervals[i][1])
        return len(heap)
