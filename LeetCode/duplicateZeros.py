class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        for i, x in enumerate([i for i in range(len(arr)) if arr[i] == 0]):
            arr.insert(x + i, 0)
            arr.pop()
