def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return int(a / gcd(a, b) * b)


print(gcd(3,11))
print(gcd(7,3))
print(gcd(9,6))
print(gcd(6,3))
print(gcd(11,15))
print(gcd(11,6))


