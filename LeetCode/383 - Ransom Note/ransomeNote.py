from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_count = Counter(magazine)
        r_count = Counter(ransomNote)
        for k, v in r_count.items():
            if k not in m_count or v > m_count[k]:
                return False
        return True
