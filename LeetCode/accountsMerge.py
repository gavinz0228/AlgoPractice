from typing import List
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        index_lookup = {}
        account_lookup = {}
        for i, accs in enumerate(accounts):
            index = []
            accs = accs[1:]
            for acc in accs:
                if acc in index_lookup:
                    index.append( index_lookup[acc] )
            if index:
                firstidx = index[0]
                for i in index[1:]:
                    if i != firstidx and i in account_lookup:
                        for acc in account_lookup[i]:
                            index_lookup[acc] = firstidx
                            account_lookup[firstidx].append(acc)
                        del account_lookup[i]
                #print(firstidx, account_lookup)
                for acc in accs:
                    index_lookup[acc] = firstidx
                    account_lookup[firstidx].append(acc)
            else:
                if i not in account_lookup:
                    account_lookup[i] = []
                for acc in accs:
                    index_lookup[acc] = i
                    account_lookup[i].append(acc)
        old_new_index = {}
        sol = []
        distinct_idx = set(index_lookup.values())
        for i, idx in enumerate(distinct_idx):
            old_new_index[idx] = i
            sol.append( [ accounts[idx][0]]  )
        for acc, oidx in index_lookup.items():
            sol[ old_new_index[oidx] ].append(acc)
        for s in sol:
            s[1:] = sorted(s[1:])
        return sol
