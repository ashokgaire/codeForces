def printUnion(arr1, arr2, m, n):
    newarr = []
    i = j = 0
    while i < m and j < n:
        if arr1[i] > arr2[j]:
            newarr.append(arr2[j])
            j +=1
        elif arr2[j] > arr1[i]:
            newarr.append(arr1[i])
            i +=1

        elif arr2[j] == arr1[i]:
            newarr.append(arr1[i])
            i +=1
            j +=1

    while i < m:
        newarr.append(arr1[i])
        i +=1

    while j < n:
        newarr.append(arr2[j])
        j +=1

    print(newarr)



arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
printUnion(arr1, arr2, m, n)