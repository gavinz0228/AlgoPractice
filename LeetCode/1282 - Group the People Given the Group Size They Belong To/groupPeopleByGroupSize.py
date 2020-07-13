import collections
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        solution = []
        group = collections.defaultdict(list)
        
        for i in range(len(groupSizes)):
            size_num = groupSizes[i]

            group[size_num].append(i)

            if len(group[size_num]) == size_num:
                solution.append(group[size_num])
                del group[size_num]
                
        return solution
