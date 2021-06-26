class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count= [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - 97] += 1
            count[ord(t[i]) - 97] -= 1
        return int(sum([abs(n)for n in count]) / 2)
