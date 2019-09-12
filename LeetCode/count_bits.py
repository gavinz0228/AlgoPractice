class Solution:
    def countBits(self, num: int) -> List[int]:
        
        dp = [0]
        cur = 1
        for i in range(1, num+1):
            log = math.log(i, 2)
            if log == math.floor(log):
                dp.append(1)
                cur = 1
            else:
                dp.append(1 + dp[cur])
                cur +=1
        return dp
