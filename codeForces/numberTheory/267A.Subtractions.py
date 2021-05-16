def process(a,b):
    mini = min(a,b)
    maxi = max(a,b)
    cnt = 0

    while maxi != mini and maxi >= 0 and mini > 0:
        cnt  += maxi//mini

        maxi = maxi % mini

        if mini > maxi:
            maxi , mini = mini, maxi
    if mini == maxi and mini != 0:
        cnt +=1
    return cnt


t = int(input())

while t> 0:
    a,b = map(int, input().split())
    print(process(a,b))
    t = -1