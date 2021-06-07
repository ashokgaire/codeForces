

def findMinLen(arr):
    return len(min(arr, key=len))


def checkCommonPrefix(list, arr, start,end):

    for i in range(len(list)):
        word = list[i]
        for j in range(start, end+1):
            if word[j] != arr[j]:
                return False
    return True
def binarySearch(arr, n):
    prefix = ""
    r = findMinLen(arr)

    l = 0
    r -=1

    while l <= r:
        mid = (l+r)//2

        if checkCommonPrefix(arr, arr[0], l , mid):
            prefix += arr[0][l:mid+1]
            l = mid+1
        else:
            r = mid -1
    return prefix


n = 3
arr = ["flower","flow","flight"]
print(binarySearch(arr, n))