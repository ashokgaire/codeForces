'''
1. You are given a number n, representing the number of elements.
2. You are given n numbers, representing the contents of array of length n.
3. You are required to print the length of longest increasing subsequence of array.

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
6
'''

def longestSubsequqnce(n,m):
    newarr = [0]*n
    newarr[0] = 1

    for i in range(1,n):
        ma = 0
        for j in range(0,i):
            if m[i] > m[j]:
                if newarr[j] > ma:
                    ma = newarr[j]
    
        newarr[i] = ma + 1
    return max(newarr)



n = int(input())
m = [0]*n
for i in range(n):
    m[i] = int(input())

print(longestSubsequqnce(n,m))

