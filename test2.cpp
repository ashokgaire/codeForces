#include<bits/stdc++.h>
using namespace std;
#define ll long long

ll gcd(ll a, ll b){
  while(b) b ^= a ^= b ^= a %= b;
    return a;
}


int main(){
  ll d[10]={0};
ll a[10], f[10]={0};
  
  ll n;cin>>n;
  assert(1 <=n and n <= 2e5);
  for(ll i=1; i<=n; i++){
    cin>>a[i];
    assert(1 <= a[i] and a[i] <= 2e5);
    f[a[i]]++;
  }
  
  ll t;cin>>t;
  
  for(ll i=1; i<=10; i++){
    for(ll j=i; j<=10; j+=i){
      d[i]+=f[j];
    }
  }
  assert(1 <= t and t <= 2e5);
  while(t--){
    ll p, q;cin>>p>>q;
    assert(1 <= p and p <= 2e5);
    assert(1 <= q and q <= 2e5);
    ll lcm = (p*q)/gcd(p,q);
    ll temp;
    if(lcm > 10)temp = 0;
    else temp=d[lcm];
    cout<<d[p]+d[q]-temp<<endl;
  }
  return 0;
}