from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        chrs = Counter(chars)
        for w in words:
            cur_count = Counter(w)
            match = True
            for k, v in cur_count.items():
                if k not in chrs or v > chrs[k]:
                    match = False
                    break
            if match:
                total += len(w)
        return total
                    
