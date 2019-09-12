from collections import deque
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        left_to_right = [nums[0]]
        right_to_left = deque( [nums[-1]])
        for i in range(1, length):
            left_to_right.append(left_to_right[-1] * nums[i])
            right_to_left.appendleft(right_to_left[0] * nums[length - 1 - i])

        result = [right_to_left[1]]
        for i in range(1, length - 1):
            result.append(left_to_right[i-1] * right_to_left[i+1] )
        result.append(left_to_right[-2])
        return result
            

"""
# Actually it doesn't allow to use division， too bad...

class Solution(object):
    def productExceptSelf(self, nums):
        
        #:type nums: List[int]
        #:rtype: List[int]

        num_zero = 0
        s = 1
        for x in nums:
            if x == 0:
                num_zero += 1
            else:
                s *= x
        if num_zero == 0:
            return [ s/x for x in nums]
        elif num_zero == 1:
            return [ s if x == 0 else 0 for x in nums]
        else:
            return [0] * len(nums)
            
"""