t = int(input())

while t > 0:
    a, b, c = map(int, input().split())
    print("1" + "0" * (a - 1), "1" * (b - c + 1) + "0" * (c - 1))
    t -=1