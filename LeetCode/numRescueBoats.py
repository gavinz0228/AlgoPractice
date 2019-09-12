class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i = 0
        j = len(people) - 1
        count = 0
        while i<= j :
            if people[i] + people[j] <= limit:
                i += 1
                j -= 1
            else:
                j -= 1
            count += 1
        return count
