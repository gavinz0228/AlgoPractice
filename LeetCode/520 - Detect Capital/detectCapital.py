class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return 1 == len(word) or word[1:].islower() if word[0].islower() else 1 == len(word) or word[1:].islower() or word[1:].isupper()
