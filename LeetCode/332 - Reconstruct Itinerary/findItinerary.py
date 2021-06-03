'''
332. Reconstruct Itinerary
Medium

2793

1293

Add to List

Share
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
Accepted
216,659
Submissions
562,671
'''

from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.graph = defaultdict(list)
        self.tickets = tickets
        self.path_used = 0
        self.sol = None
        for t in self.tickets:
            self.graph[t[0]].append(t[1])
        
        self.backtrack("JFK", ["JFK"])
        return self.sol
    
    def backtrack(self, curr, curr_acc):
        targets = sorted(self.graph[curr])
        for tar in targets:
            if self.path_used + 1  == len(self.tickets):
                self.sol = curr_acc + [tar]
                return
            self.graph[curr].remove(tar)
            self.path_used +=1
            self.backtrack(tar, curr_acc + [tar])
            self.path_used -=1
            if self.sol:
                return
            self.graph[curr].append(tar)
