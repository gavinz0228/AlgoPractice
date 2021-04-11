# Complete the acmTeam function below.
def acmTeam(topic):
    max_val = 0
    max_num = 0
    for i in range(0, len(topic) - 1):
        for j in range(i + 1, len(topic)):
            val = sum([1 for k in range(len(topic[i])) if topic[i][k] == '1' or topic[j][k] == '1'])
            if val > max_val:
                max_val = val
                max_num = 1
            elif val == max_val:
                max_num += 1
    return [max_val, max_num]
