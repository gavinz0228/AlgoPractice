class Solution(object):
    def canPartition(self, nums):
        lookup = set([0])
        for n in nums:
            new_lookup = set()
            for lookup_sum in lookup:
                new_lookup.add(lookup_sum + n)
                new_lookup.add(lookup_sum - n)
            lookup = new_lookup
            print(lookup)
        return 0 in lookup

#res = Solution().canPartition([1,1,2,5,5])
#print(res)