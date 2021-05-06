
def solve(arr,n):
    ans = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ans[i][j] = arr[j][(i+j) % n]

    return ans

def show(arr,n):

    if n == 1:
        print("1")
        return
    if n == 2:
        print("-1")
        return
    res = solve(arr,n)

    for i in range(n):
        for j in range(n):
            print(res[i][j], end= " ")
        print()


def process(n):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    c = 1

    for i in range(n):
        for j in range(n):
            arr[j][i] = c
            c += 1
    return arr



t = int(input())
while(t>0):
    n = int(input())
    arr =process(n)
    show(arr,n)
    t -=1






