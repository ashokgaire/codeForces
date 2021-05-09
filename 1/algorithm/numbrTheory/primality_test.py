def test(n):
    if n ==1:
        return "no"

    for j in range(2,n):
        if n % j == 0:
            return "no"
        j *=j
    return "yes"

t = int(input())

while t > 0:
    n = int(input())
    print(test(n))


    t -=1