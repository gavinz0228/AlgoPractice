class Solution:
    def toLowerCase(self, str: str) -> str:
        new = []
        for x in str:
            n = ord(x)
            if n >= 65 and n<= 90:
                n += 32
            new.append(chr(n))
        return "".join(new)
        
