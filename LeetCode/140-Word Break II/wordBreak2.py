class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        l = len(s)
        mem = {}
        def dfs(i = 0):
            if i in mem:
                return mem[i]
            mem[i] = []
            curr = mem[i]
            for w in wordDict:
                wl = len(w)
                if i+ wl  > l:
                    continue
                if s[i:].startswith(w):
                    if i+ wl  == l:
                        curr.append([w])
                    else:
                        for comb in dfs(i + wl):
                            curr.append([w] + comb)
            return curr
        
        return [ " ".join(w) for w in dfs()]
        
