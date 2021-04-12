
"""
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

Example


There are two numbers between the arrays:  and .
, ,  and  for the first value.
,  and ,  for the second value. Return .

Function Description

Complete the getTotalX function in the editor below. It should return the number of integers that are betwen the sets.

getTotalX has the following parameter(s):

int a[n]: an array of integers
int b[m]: an array of integers
Returns

int: the number of integers that are between the sets
"""
def getTotalX(a, b):
    # Write your code here
    min_val = min(a)
    max_val = max(b)
    res = 0
    for i in range(min_val, max_val + 1):
        if all([ i % n == 0 for n in a]) and all([n % i == 0 for n in b]):
            res += 1
    return res
    
