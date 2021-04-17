"""
Lauren has a chart of distinct projected prices for a house over the next several years. She must buy the house in one year and sell it in another, and she must do so at a loss. She wants to minimize her financial loss.

Example

Her minimum loss is incurred by purchasing in year  at  and reselling in year  at . Return .

Function Description

Complete the minimumLoss function in the editor below.

minimumLoss has the following parameter(s):

int price[n]: home prices at each year
Returns

int: the minimum loss possible
Input Format

The first line contains an integer , the number of years of house data.
The second line contains  space-separated long integers that describe each .

Constraints

All the prices are distinct.
A valid answer exists.
Subtasks

 for  of the maximum score.
Sample Input 0

3
5 10 3
Sample Output 0

2
Explanation 0

Lauren buys the house in year  at  and sells it in year  at  for a minimal loss of .

Sample Input 1

5
20 7 8 2 5
Sample Output 1

2
Explanation 1

Lauren buys the house in year  at  and sells it in year  at  for a minimal loss of .
"""

# Complete the minimumLoss function below.
def minimumLoss(price):
    lookup = {}
    for i in range(len(price)):
        lookup[price[i]] = i
    res = float('inf')
    price = sorted(price, reverse = True)
    for i in range(len(price) - 1):
        if lookup[price[i+1]] > lookup[price[i]]:
            cur = price[i] - price[i+1]
            if cur < res:
                res = cur
    return res
    
