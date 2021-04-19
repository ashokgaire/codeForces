#include <bits/stdc++.h>
#define MAXN 100005
#define K 25
#define ll long long int
using namespace std;
 
int tc=1,n,q,arr[MAXN+1],st[MAXN][K],lg[MAXN+1],curr,previous,curr_gcd;
map<int,ll> cnt;
 
int gcd(int L,int R)
{
    int j = lg[R - L + 1];
    return __gcd(st[L][j], st[R - (1 << j) + 1][j]);
}
 
int getMid(int i)
{
    int l = curr , r = n;
    while(l<r-1)
    {
        int mid = (l+r)/2;
        if(gcd(i,mid) == curr_gcd)
            l = mid;
        else 
            r = mid;
    }
    return r;
}
 
void preprocess(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    lg[1] = 0;
    for (int i = 2; i <= MAXN; i++)
        lg[i] = lg[i/2] + 1;
}
 
void input()
{
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
        scanf("%d",arr+i);
}
 
void solve()
{       
    //preprocessing 1
    for (int i = 1; i <= n; i++)
        st[i][0] = arr[i];
 
    for (int j = 1; j <= K; j++)
        for (int i = 1; i + (1 << j) <= n+1; i++)
            st[i][j] = __gcd(st[i][j-1], st[i + (1 << (j - 1))][j - 1]);
 
    //preprocessing 2
    for(int i=1;i<=n;i++)
    {
        curr = previous = i;
        curr_gcd = arr[i];
        while(curr < n)
        {
            curr = getMid(i);
            cnt[curr_gcd] += curr - previous;
            curr_gcd = gcd(i,curr);
            previous = curr;
            if(curr_gcd == 1)
                break;
        }
        cnt[curr_gcd] += n - curr + 1;
    }
 
 
    // solution
    scanf("%d",&q);
    for(int i=0;i<q;i++)
    {
        int x;
        scanf("%d",&x);
        printf("%lld\n",cnt[x]);
    }
    //cerr << (__gcd(__gcd(2,6),3)) << endl;
}
 
int main()
{
    preprocess();
    while(tc--){
        input();
        solve();
    }
    return 0;
}