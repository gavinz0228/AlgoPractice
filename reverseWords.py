class Solution:
    def reverseWords(self, s: str) -> str:
        parts = s.split(" ")
        return " ".join([ p for p in parts[::-1] if p ])
