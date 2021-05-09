/*

Algorithm

The algorithm is extremely simple:

gcd(a,b)={a,gcd(b,amodb),if b=0otherwise.

Implementation

int gcd (int a, int b) {
    if (b == 0)
        return a;
    else
        return gcd (b, a % b);
}

It turns out, that you can design a fast GCD algorithm that avoids modulo operations. It's based on a few properties:

    If both numbers are even, then we can factor out a two of both and compute the GCD of the remaining numbers: gcd(2a,2b)=2gcd(a,b)

.
If one of the numbers is even and the other one is odd, then we can remove the factor 2 from the even one: gcd(2a,b)=gcd(a,b)
if b
is odd.
If both numbers are odd, then subtracting one number of the other one will not change the GCD: gcd(a,b)=gcd(b,a−b)

    (this can be proven in the same way as the correctness proof of the normal algorithm)

Using only these properties, and some fast bitwise functions from GCC, we can implement a fast version:


*/

#include <bits/stdc++.h>

using namespace std;

int gcd(int a, int b)
{
    if(!a || !b)
        return a | b;
    
    unsigned shift = __builtin_ctz(a | b);

    a >>= __builtin_ctz(a);

    do
    {
        b >>= __builtin_ctz(b);
        if (a > b)
            {
                int temp = b;
                b = a;
                a =temp;
            }
        b -=a;
    } while (b);
    return a << shift;
}

int main()
{
    std::cout << gcd(4,8);
    return 0;
}