import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hlist = nums[:k]
        heapq.heapify(hlist)
        for i in range(k, len(nums)):
            heapq.heappush(hlist,  nums[i])
            heapq.heappop(hlist)
        return   heapq.heappop(hlist)
        