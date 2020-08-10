"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mem = {}
        for emp in employees:
            mem[emp.id] = emp
            
        def dfs(eid):
            total = mem[eid].importance
            for sub in mem[eid].subordinates:
                total += dfs(sub)
            return total
        return dfs(id)
            
            
            
