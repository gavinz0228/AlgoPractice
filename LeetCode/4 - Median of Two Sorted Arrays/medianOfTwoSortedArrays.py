class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        c1 = 0 
        c2 = 0
        is_whole = True
        last_num = 0
        mid_index = int( (l1+l2) /2 )
        if (l1 + l2) % 2 == 0:
            is_whole = False
            mid_index = mid_index - 1
        for i in range(l1 + l2):
            smaller = None
            if c1 >= l1:
                smaller = nums2[c2]
                c2 += 1
            elif c2 >= l2:
                smaller = nums1[c1]
                c1 += 1
            elif nums1[c1] < nums2[c2]:
                smaller = nums1[c1]
                c1 += 1
            else:
                smaller = nums2[c2]
                c2 += 1

            if i == mid_index:
                if is_whole:
                    return smaller
                else:
                    last_num = smaller
                    continue
            elif i == mid_index + 1:
                return (smaller + last_num) / 2
