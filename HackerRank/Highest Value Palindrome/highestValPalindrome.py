"""
Palindromes are strings that read the same from the left or right, for example madam or 0110.

You will be given a string representation of a number and a maximum number of changes you can make. Alter the string, one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes. The length of the string may not be altered, so you must consider 's left of all higher digits in your tests. For example  is valid,  is not.

Given a string representing the starting number, and a maximum number of changes allowed, create the largest palindromic string of digits possible or the string '-1' if it is not possible to create a palindrome under the contstraints.

Example


Make  replacements to get .



Make  replacement to get .

Function Description

Complete the highestValuePalindrome function in the editor below.

highestValuePalindrome has the following parameter(s):

string s: a string representation of an integer
int n: the length of the integer string
int k: the maximum number of changes allowed
Returns

string: a string representation of the highest value achievable or -1
"""
# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    s = list(s)
    mid = int((n -1) / 2)
    l = len(s)
    spots = []
    vals = []
    for i in range(mid + 1):
        if s[i] > s[l - i -1]:
            spots.append(l - i -1)
            vals.append(s[i])
        elif s[i] < s[l - i -1]:
            spots.append(i)
            vals.append(s[l - i -1])
                
    if k < len(spots):
        return '-1'
    changed = set()

    for i in range(len(spots)):
        s[spots[i]] = vals[i]
        changed.add(spots[i])
    k = k - len(changed)
    
    #it's alread a palindrom, now it's trying to replace numbers with 9
    for i in range(mid + 1):
        if k == 0:
            break
        #skip the ones that are 9 already
        if s[i] != '9':
            #one of them has been changed, change both side only count as 1
            if i in changed or l - i - 1 in changed:
                s[i] = '9'
                s[l - i - 1] = '9'
                k -= 1
            else:
            #if it's greater than 1, and both side of this spot is untouch, 
            #change both side to 9
                if k > 1:
                    s[i] = '9'
                    s[l - i - 1] = '9'
                    k -= 2
                else:
                    break                
    if k >= 1 and l % 2 == 1:
        s[mid] = '9'
    return "".join(s)
