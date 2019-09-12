
def answer(l):
    ln = len(l)
    l.sort(reverse= True)
    if sum(l) % 3 == 0:
        return int("".join([chr(n + 48) for n in l]))
    
    for i in range(1, ln):
        res = []
        for nums in combinations(l, ln - i):
            if sum(nums) % 3 == 0:
                nums.sort(reverse = True)
                res.append("".join([chr(48+n) for n in nums]))
        if res:
            return int(max(res))

def combinations(l, n):
    if n == 0:
        return []
    if n == 1:
        return [[x] for x in l]
    res = []
    for i in range(len(l)):
        for s in combinations( l[i+1:] , n - 1):
            res.append([l[i]] + s)
    return res
#print(combinations([1,2,3,4],3))
print(answer([1]))
