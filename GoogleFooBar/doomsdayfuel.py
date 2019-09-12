class Fractional:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator
    def mul(self, factional):
        return Fractional(self.nominator * factional.nominator, self.denominator * factional.denominator )
    def div (self, fractional):
        return Fractional(self.nominator * fractional.denominator, self.denominator * fractional.nominator)
    def __str__(self):
        return str(self.nominator) + "/" + str(self.denominator)
    def __repr__(self):
        return self.__str__()
def findNoneCircle(m, start, end, row_sums, terminals):
    visited = set()
    stack = []
    row_len = len(m[0])
    #(prob, state/row, path)
    task = (Fractional(1,1), 0, [0])
    stack.append(task)
    visited.add(0)
    solutions = []
    while True:
        if not stack:
            break
        curr_task = stack.pop()
        curr_state = curr_task[1]
        curr_prob = curr_task[0]
        curr_path = curr_task[2]
        for i in range(row_len):
            if not m[curr_state][i] == 0:
                if i not in visited:
                    visited.add(i)
                    #add task
                    if not i in terminals:
                        
                        p = Fractional(m[curr_state][i], row_sums[curr_state] )
                        new_prob = curr_prob.mul(p)
                        new_path = list(curr_path)
                        new_path.append(i)
                        stack.append((new_prob, i, new_path))
                    else:
                        if i == end:
                            p = Fractional(m[curr_state][i], row_sums[curr_state] )
                            end_prob = curr_prob.mul(p)
                            new_path = list(curr_path)
                            new_path.append(i)
                            solutions.append((end_prob, tuple(new_path) ))
    print("terminals", terminals)
    print(solutions)

def find(m, start, end, row_sums, terminals):
    findNoneCircle(m, start, end, row_sums, terminals)

def answer(m):
    ln = len(m)
    
    row_sums = [sum(row) for row in m]
    terminals = [ i for i, s in enumerate(row_sums) if s == 0]
    prob = []
    for i in terminals:
        p = find(m, 0, i, row_sums, terminals)
        prob.append(p)
      

m = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

print(answer(m))
