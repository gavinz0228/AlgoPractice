from collections import defaultdict


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(int)
        to_trust = defaultdict(int)
        max_trusted_num = 0
        most_trusted_person = 1
        for pair in trust:
            trusted[pair[1]] += 1
            to_trust[pair[0]] += 1
            if trusted[pair[1]] > max_trusted_num:
                max_trusted_num = trusted[pair[1]]
                most_trusted_person = pair[1]
        if max_trusted_num == N - 1 and to_trust[most_trusted_person] == 0:
            return most_trusted_person
        else:
            return -1
