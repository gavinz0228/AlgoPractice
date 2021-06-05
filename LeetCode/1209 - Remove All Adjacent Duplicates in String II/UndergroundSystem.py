'''
1209. Remove All Adjacent Duplicates in String II
Medium

1621

34

Add to List

Share
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
 

Constraints:

1 <= s.length <= 105
2 <= k <= 104
s only contains lower case English letters.
Accepted
102,031
Submissions
178,387
'''

from collections import defaultdict
class UndergroundSystem:

    def __init__(self):
        self.status = {}
        self.calc = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.status[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startT = self.status.pop(id, None)
        self.calc[(startStation, stationName)].append(t - startT)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        ts = self.calc[(startStation, endStation)]
        return sum(ts)/len(ts)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
