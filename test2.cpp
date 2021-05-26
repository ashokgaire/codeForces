#include <bits/stdc++.h>
using namespace std;

#define ll long long


int main()
{
    int n , i; 
    cin >> n;
    ll maxi = 0;
    vector<ll> v(n);

    for(i=0; i < n; i++)
    {
        cin >> v[i];
        maxi = max(maxi, v[i]);
    }
    radixSort(v,maxi);
    return 0;
}