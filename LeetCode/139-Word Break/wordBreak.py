class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        des = len(s) - 1
        visited = set()
        nex_start = [0]
        while nex_start:
            new_nex_start = []
            for sp in nex_start:
                for w in wordDict:
                    if s[sp:].startswith(w):
                        p = sp + len(w)
                        if p not in visited:
                            visited.add(p)
                            new_nex_start.append(p)
                            
            nex_start = new_nex_start
        if des + 1 in visited:
            return True
        else:
            return False
                            
