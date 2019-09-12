class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x:(x[0], x[1]))
        length = len(people)
        q = [None] * length
        for p in people:
            count = p[1]
            i = 0
            while i < length:
                if not q[i] or q[i][0] == p[0]:
                    if count == 0:
                        break
                    else:
                        count -= 1
                i+= 1
            q[i] = p
        return q