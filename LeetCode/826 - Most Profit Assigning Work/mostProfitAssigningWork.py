class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        sol = 0
        jobs = [(difficulty[i], profit[i], i) for i in range(len(profit))]
        length = len(jobs)
        jobs.sort(reverse=True, key=lambda j: (j[1], j[0]))
        worker.sort(reverse=True)
        start_point = 0
        for md in worker:
            i = start_point
            while i < length:
                if jobs[i][0] <= md:
                    sol += jobs[i][1]
                    start_point = i
                    break
                i += 1
        return sol
