import math
def answer(num):
    if num in ['1', '0']:
        return 0
    num = int(num)
    root = math.log(num, 2)
    map = {}
    if root == int(root):
        return int(root)
    min_ops = None
    stack = []
    stack.append((0,num))
    while stack:
        task = stack.pop()
        if task[1] % 2 == 0:
            if task[1] == 2:
                if not min_ops:
                    min_ops = task[0] + 1
                elif task[0] < min_ops:
                    min_ops = task[0] + 1
            else:
                new_task = (task[0] + 1,task[1] / 2)

                if not new_task[1] in map:
                    map[new_task[1]] = new_task[0]
                    stack.append(new_task)
                elif map[new_task[1]] > new_task[0]:
                    map[new_task[1]] = new_task[0]
                    stack.append(new_task)
        else:
            new_task = (task[0] + 1,task[1] + 1)
            if not new_task[1] in map:
                map[new_task[1]] = new_task[0]
                stack.append(new_task)
            elif map[new_task[1]] > new_task[0]:
                map[new_task[1]] = new_task[0]
                stack.append(new_task)
            new_task =(task[0] + 1,task[1] - 1)
            if not new_task[1] in map:
                map[new_task[1]] = new_task[0]
                stack.append(new_task)
            elif map[new_task[1]] > new_task[0]:
                map[new_task[1]] = new_task[0]
                stack.append(new_task)

    return min_ops