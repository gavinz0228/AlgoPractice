def permute(ls):
    l = len(ls)
    if l == 0:
        return []
    if l == 1:
        return [ls]
    sol = []
    for i in range(l):
        sub = permute(ls[:i] + ls[i+1:])
        for x in sub:
            sol.append(x + [ls[i]])
    return sol
            
print(permute([1,2,3]))
