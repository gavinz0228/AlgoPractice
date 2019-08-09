from typing import List
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lookup = {}
        sol = []
        for i, c in enumerate(S):
            if c in lookup:
                lookup[c][1] = i
            else:
                lookup[c] = [i, i]
        group_len = len(lookup)
        groups = list(lookup.values())
        groups.sort()
        i = 1
        cur_min = groups[0][0]
        cur_max = groups[0][1]
        while i < group_len:
            if groups[i][0] < cur_max:
                cur_max = max(cur_max, groups[i][1])
                cur_min = min(cur_min, groups[i][0])
                
            else:
                sol.append(cur_max + 1 - cur_min)
                cur_min = groups[i][0]
                cur_max = groups[i][1]
            i += 1
        
        sol.append(cur_max + 1 - cur_min)
        return sol