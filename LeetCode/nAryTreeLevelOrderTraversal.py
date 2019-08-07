class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        sol = []
        q = [root]
        while q:
            newq = []
            cur = []
            for n in q:
                cur.append(n.val)
                for c in n.children:
                    newq.append(c)
            sol.append(cur)   
            q = newq 
        return sol
