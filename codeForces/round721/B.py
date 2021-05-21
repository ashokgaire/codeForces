def check(s):
    n = len(s)
    cnt = 0
    for i in range(n):
        if s[i] == 1:
            cnt +=1
    return n == cnt

def checkPalindrome(s):
    return s == s[::-1]

def process(a):
    cost = [0,0]
    last = 0
    turn = 0

    while not check(a):
        if checkPalindrome(a):
            for i in range(len(a)):
                if a[i] == 0:
                    last = 0
                    a[i] = 1
                    cost[turn] +=1
                    if turn == 0:
                        turn +=1
                    else:
                        turn -=1
                    break
        elif not checkPalindrome(a) and not last:
            a = a[::-1]
            last = 1
            if turn == 0:
                turn +=1
            else:
                turn -=1
        else:
            for i in range(len(a)):
                if a[i] == 0:
                    last = 0
                    a[i] = 1
                    cost[turn] +=1
                    if turn == 0:
                        turn +=1
                    else:
                        turn -=1
                    break
    if cost[0] > cost[1]:
        return "BOB"
    else:
        return "ALICE"



t = int(input())
while t > 0:

    n = int(input())
    s = list(map(int, input()))
    print(process(s))
    t -=1