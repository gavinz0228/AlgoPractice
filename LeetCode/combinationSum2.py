class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.candidates = candidates
        self.length = len(candidates)
        self.solutions = set()
        self.target = target
        self.aux([], 0, 0)
        return list(self.solutions)
    def aux(self, cur_sol, cur_sum , i):
        if i == self.length:
            return
        temp = cur_sum + self.candidates[i]
        if temp == self.target:
            self.solutions.add(tuple(cur_sol + [self.candidates[i]]))
            return
        elif temp > self.target:
            return
        else:
            self.aux(cur_sol + [self.candidates[i]], temp, i + 1)
            self.aux(cur_sol, cur_sum, i + 1)
