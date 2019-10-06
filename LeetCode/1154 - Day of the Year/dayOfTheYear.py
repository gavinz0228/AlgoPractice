class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        parts = date.split('-')
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        base = (0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
        res = base[month]
        if month <= 2:
            return res + day
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return res + day + 1
        else:
            return res + day