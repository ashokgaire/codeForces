'''
iven two binary arrays arr1[] and arr2[] of same size n. Find length of the longest common span (i, j) where j >= i such that arr1[i] + arr1[i+1] + …. + arr1[j] = arr2[i] + arr2[i+1] + …. + arr2[j].
'''
def longestCommonSum(arr1, arr2, n):
    maxlen = 0
    diff = {}
    sum1 = 0
    sum2 = 0
    for i in range(n):
        sum1 +=arr1[i]
        sum2 += arr2[i]

        difflen = sum1 - sum2

        if difflen == 0:
            maxlen = i + 1

        elif difflen not in diff:
            diff[difflen] = i
        else:
            length = i - diff[difflen]
            maxlen = max(length, maxlen)

    return maxlen





arr1 = [0, 1, 0, 1, 1, 1, 1]
arr2 = [1, 1, 1, 1, 1, 0, 1]
n = len(arr1)
print("Length of the longest common span with same "
            "sum is",longestCommonSum(arr1, arr2, n))