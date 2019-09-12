import functools
def answer(m):
    row_sum = [ sum(row) for row in m]
    print(row_sum)
    denominator = functools.reduce(lambda x, y: x*y, filter(lambda x: True if not x == 0 else False ,row_sum))
    print(denominator)
print(answer([
    [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
    [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
    [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
    [0,0,0,0,0,0],  # s3 is terminal
    [0,0,0,0,0,0],  # s4 is terminal
    [0,0,0,0,0,0],  # s5 is terminal
]))