class Solution:
    def validIPAddress(self, IP: str) -> str:
        idx = -1
        try:
            idx = IP.index(".")
        except ValueError:
            pass
        
        if idx > -1:
            parts = IP.split(".")
            if self.checkIPv4(parts):
                return "IPv4"
            else:
                return "Neither"
        else:
            parts = IP.split(":")
            if self.checkIPv6(parts):
                return "IPv6"
            else:
                return "Neither"
    def checkIPv4(self, parts):
        if len(parts) != 4:
            return False
        for p in parts:
            pl= len(p)
            if pl > 3 or pl< 1 or p.startswith("-"):
                return False
            if pl> 1 and p.startswith("0"):
                return False
            try:
                n = int(p)
                
            except:
                return False
            if n < 0 or n > 255:
                return False
        return True
    def checkIPv6(self, parts):
        if len(parts) != 8:
            return False
        for p in parts:
            pl = len(p)
            if pl> 4 or pl < 1 or p.startswith("-"):
                return False
            try:
                n = int(p, 16)
            except:
                return False
            if n > 65535 or n < 0:
                return False
        return True
        
            
        
