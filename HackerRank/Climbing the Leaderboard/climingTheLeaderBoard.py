def climbingLeaderboard(ranked, player):
    # Write your code here
    lookup = {}
    lookup[ranked[0]] = 1
    offset = 0
    for i in range(1, len(ranked)):
        if ranked[i] == ranked[i-1]:
            offset += 1
        else:
            lookup[ranked[i]] = i - offset + 1

    r = len(ranked) - 1 
    p_len = len(player)
    p = 0
    res = []
    
    while p < p_len:
        if r < 0:
            res.append(1)
            p += 1
        else:
            if player[p] == ranked[r]:
                res.append(lookup[player[p]])
                r -= 1
                p += 1
            elif player[p] < ranked[r]:
                res.append(lookup[ranked[r]] + 1)
                p += 1
            else:  
                r -= 1
    return res
