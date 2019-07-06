from bisect import bisect

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        lookup = {}
        length = len(nums)
        for i, x in enumerate(nums):
            if x not in lookup:
                lookup[x] = [i]
            else:
                lookup[x].append(i)
        sorted_list = sorted(nums)
        for i, x in enumerate(nums):
            idx = bisect(sorted_list, x)
            cur_idx = idx
            while cur_idx < length:
                n = sorted_list[cur_idx]
                if n - x > t:
                    break
                for ti in lookup[n]:
                    if abs(ti - i) > k:
                        break
                    if ti != i and abs(ti - i) <= k:
                        return True
                cur_idx += 1
            idx -= 1
            while idx >= 0 :
                n = sorted_list[idx]
                if x - n > t:
                    break
                for ti in lookup[n]:
                    if ti != i and abs(ti - i) <= k:
                        return True
                idx -=  1  
        return False
