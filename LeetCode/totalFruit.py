class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        length = len(tree)
        cur = []
        count = {}
        consec = {}
        reach_end = False
        last = tree[0]
        for i in range(length):
            n = tree[i]
            if len(count) == 2 and n not in count:
                break
            if n not in count:
                count[n] = 1
                consec[n] = 1
                cur.append(n)
            else:
                count[n] += 1
                if n == last:
                    consec[n] +=1
                else:
                    consec[n] = 1                    
            if i == length -1:
                reach_end = True
            last = n
            
        max_sum = sum(count.values())
        if reach_end:
            return max_sum
        cur = list(count.keys())
        for j in range(i, length):
            n = tree[j]
            prev = tree[j - 1]
            
            if n == last:
                consec[n] += 1
            else:
                consec[n] = 1
                
            if n in cur:
                count[n] += 1
            else:
                old = None
                if prev == cur[1]:
                    old = cur.pop(0)
                else:
                    old = cur.pop()
                
                count[cur[0]] = consec[cur[0]]
                cur.append(n) 
                del count[old]
                del consec[old]
                count[n] = 1
                consec[n] = 1
            
            s = sum(count.values())
            if s > max_sum:
                max_sum = s 
            last = n
        s = sum(count.values())
        if s > max_sum:
            max_sum = s
        return max_sum
            
