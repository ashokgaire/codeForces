
def process(n):
    if n <= 9:
        return n

    if n <=100:
        return 9 + int(n/11)

    if n <=1000:
        return 18 + int(n/111)

    if n <=10000:
        return 27 + int(n/1111)

    if n <=100000:
        return 36 + int(n/11111)

    if n <= 1000000:
        return 45 + int(n/111111)

    if n <= 10000000:
        return 54 + int(n/1111111)

    if n <= 100000000:
        return 63 + int(n / 11111111)
    if n <= 1000000000:
        return 72 + int(n / 111111111)


t = int(input())
while(t>0):
    n = int(input())
    print(process(n))
    t -=1






