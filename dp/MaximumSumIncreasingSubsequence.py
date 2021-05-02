'''
1. You are given a number n, representing the number of elements.
2. You are given n numbers, representing the contents of array of length n.
3. You are required to print the sum of elements of the increasing subsequence with maximum sum for the array.

Input Format

A number n
.. n more elements

Output Format

A number representing the sum of elements of the increasing subsequence with maximum sum for the array.


Constraints

0 <= n <= 20
0 <= n1, n2, .. <= 100

Sample Input

10
10
22
9
33
21
50
41
60
80
1

Sample Output
255



'''

def maximumSum(n,m):
    table = [0]*n
    table[0] = m[0]


    for i in range(1,n):
        ma = 0 
        for j in range(0,i):
            if m[i] >= m[j]:
                if ma == 0:
                    ma = table[j]
                elif table[j] > ma:
                    ma = table[j] 

        table[i] = m[i] + ma
    print(table)
    return max(table)



n = int(input())
m = [0]*n
for i in range(n):
    m[i] = int(input())

print(maximumSum(n,m))