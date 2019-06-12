class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        mb = []
        nb = []
        while m!= 0:
            mb.append( m % 2 )
            m = int(m / 2)
        while n!= 0:
            nb.append(n % 2)
            n = int(n / 2)
        ml = len(mb)
        nl = len(nb)
        if ml != nl:
            return 0
        result = []
        for i in range(ml -1, -1, -1):
            if mb[i] == nb[i]:
                result.append(str(mb[i]) )
            else:
                break
        result.extend( ['0'] * (ml - len( result )) )
        if not result:
            return 0
        return int("".join(result), 2)
