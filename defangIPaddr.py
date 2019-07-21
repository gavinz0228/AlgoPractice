class Solution:
    def defangIPaddr(self, address: str) -> str:
        parts = address.split(".")
        return "[.]".join(parts)
        
