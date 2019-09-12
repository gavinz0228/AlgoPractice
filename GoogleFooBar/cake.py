def chop_comp(s, num_chop, l):
    val_comp = [ s[i*l: (1+i)*l] for i in range(num_chop)]
    return all( x == val_comp[0] for x in val_comp)
def answer(s):
    l = len(s)
    for i in range(1,l):
        chop = int(l / i)
        if chop * i == l:
            
            if chop_comp(s, chop, i ):
                return chop
    return 0
print(answer("abvabv"))