class Solution:
    def __init__(self):
        arr = [1]
        for i in range(5):
            arr.append(arr[-1]*2)
        self.arr = arr

    def readBinaryWatch(self, num: 'int') -> 'List[str]':
        solutions = []
        hourArr = self.arr[0:4]
        minuteArr = self.arr
        for i in range(num + 1 ):
            left = self.com(hourArr, i)
            right = self.com(minuteArr, num - i)
            for l in left:
                for r in right: 
                    if l<12 and r<60:
                        solutions.append(str(l) +":"+'{0:02}'.format(r) )
        return solutions

    def com(self, baseArr, toChoose):
        sol = []
        l = len(baseArr)
        if toChoose == 0 :
            return [0]
        if l == 0 or toChoose > l:
            return []
        if l == toChoose:
            return [sum(baseArr)]
        else:
            chooseResult = self.com(baseArr[1:], toChoose - 1)
            for r in chooseResult:
                sol.append(baseArr[0] + r)
            notChooseResult = self.com(baseArr[1:], toChoose)
            for r in notChooseResult:
                sol.append(r)  
        return sol         

result = Solution().readBinaryWatch(5)
