from collections import defaultdict
class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        
        length = len(values)
        ls = [ ( values[i],labels[i]) for i in range(length)]
        ls.sort(reverse = True)
        ht = defaultdict(int)
        result = 0
        count = 0 
        for v, l in ls:
            if count == num_wanted:
                break
            if ht[l] < use_limit:
                ht[l] += 1
                result += v
                count +=1
        return result