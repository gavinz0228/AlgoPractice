class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        curr_max = max(candies)
        solution = []
        for i in range(len(candies)):
            if candies[i] == curr_max:
                solution.append(True)
            else:
                if candies[i] + extraCandies >= curr_max:
                    solution.append(True)
                else:
                    solution.append(False)
        return solution
