class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        lookup = {}
        existed = set()
        words = str.split(" ")
        if len(words) != len(pattern):
            return False
        for i, p in enumerate(pattern):
            if p not in lookup:
                if words[i] in existed:
                    return False
                lookup[p] = words[i]
                existed.add(words[i])
            else:
                if words[i] != lookup[p]:
                    return False
        return True
