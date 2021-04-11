#include <bits/stdc++.h>

using namespace std;


long long binpow(long long a, long long b)
{
    if (b == 0)
    {
        return 1;
    }
    long long res = binpow(a,b/2);
    if (b % 2)
    {
        return res*res*a;
    }
    else return res*res;
}

int main()
{
    long long result =1 ;
    long long n;
    long long k ;
    cin >> n;
    k = 2*n -2;
    
    result = 6*(binpow(4,n-3)*4)+(n-3)*9*binpow(4,n-3);
    cout << result << endl;


    
    

    


}