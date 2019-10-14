class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        first, second, third =[ tuple(p) for p in points]
        if first == second or second == third or first == third:
            return False
        product1 = (first[0] - second[0]) * (first[1] - third[1])
        product2 = (first[0] - third[0]) * (first[1] - second[1])
        return product1 != product2
