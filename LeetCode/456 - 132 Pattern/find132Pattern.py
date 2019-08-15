from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if not nums:
            return False
        length = len(nums)
        leftToRight = [nums[0]]
        stack = [nums[-1]]
        for i in range(1, length):
            leftToRight.append(min(nums[i], leftToRight[-1]))
        for i in range(length -2 , 0, -1 ):
            #print(i, stack)
            if nums[i] > leftToRight[i-1] and stack and nums[i] > stack[-1]:
                while stack and stack[-1] < nums[i]:
                    n = stack.pop()
                    if n > leftToRight[i-1] and n < nums[i]:
                        return True
                stack.append(nums[i])
            else:
                stack.append(nums[i])
        return False