public class Solution {
    public int ThirdMax(int[] nums) {
        int? first = null;
        int? second = null;
        int? third = null;
        
        foreach(int n in nums)
        {
            if(first == null || n >= first)
            {
                if(first == n)
                    continue;
                third = second;
                second = first;
                first = n;
            }
            else if(second == null || n < first && n >= second)
            {
                if(second == n)
                    continue;
                third = second;
                second = n;      
            }
            else if(third == null || n < second && n >= third)
            {
                if(third == n)
                    continue;
                third = n;
            }
        }
        if(third  == null)
        {
            return first.Value;
        }
        else
            return third.Value;
    }
}