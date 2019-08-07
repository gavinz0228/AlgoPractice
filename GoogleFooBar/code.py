def answer(ls):
    ln = len(ls)
    count = 0
    map= {v:i for i, v in enumerate(ls)}
    max_val = max(ls)
    min_val = min(ls)
    for i in range(1, ln - 1):
        before_count = 0
        after_count = 0
        for div_id in range(i):
            if ls[i] % ls[div_id] == 0:
                before_count += 1
        if before_count == 0:
            continue
        for div_id in range(i + 1, ln):
            if ls[div_id] % ls[i]  == 0:
                after_count += 1
        if not after_count == 0:
            count += before_count * after_count
    return count