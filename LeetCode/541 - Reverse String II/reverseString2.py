import math


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)
        parts = math.ceil(length / k)
        res = []
        for i in range(parts):
            if i % 2 == 0:
                res.append(s[i*k:(i+1)*k][::-1])
            else:
                res.append(s[i*k:(i+1)*k])
        return "".join(res)
