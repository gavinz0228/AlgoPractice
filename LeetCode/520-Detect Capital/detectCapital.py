class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        wl = len(word)
        if wl ==0 :
            return False
        
        def isCap(letter):
            asci = ord(letter)
            return asci >= 65 and asci <= 90
        
        capCount = 0
        for c in word:
            if isCap(c):
                capCount += 1
    
        initCap = isCap(word[0])
        
        return (initCap and (capCount == 1 or capCount == wl)) or capCount == 0
        
