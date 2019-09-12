def answer(l, t):
    ln = len(l)
    if ln == 0:
        return [-1, -1]
    if ln == 1:
        if l[0] == t:
            return [0, 0]
        else:
            return [-1, -1]
    for i in range(ln):
        for j in range(1, ln - i + 1):
            if sum(l[i:i+j]) == t:
                return [i, i + j - 1]
    return [-1, -1]
print(answer([1,4,5,3], 12))