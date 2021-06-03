#include<bits/stdc++.h>
using namespace std;
#define ll long long

struct Segment
{
  int size;
  vector<int> arr;
  void init(int n)
  {
    size =1;
    while (size < n)
    {
      size *=2;
    }
    arr.assign(2*size,0LL);
    

  }

  void build(vector<int> a, int x, int lx, int rx)
  {
    if (rx- lx == 1)
    {
      if (lx < (int) a.size()){
        arr[x] = a[lx];

      }
      return ;
    }

    int m = (lx + rx)/2;
    build(a,2*x+1, lx,m);
    build(a,2*x+2, m , rx);
    arr[x] = min(arr[2*x+1], arr[2*x+2]);
  }

  void build(vector<int> a)
  {
    build(a,0,0,size);
  }


  void set(int i , int v , int x, int lx, int rx)
  {
    if(rx - lx == 1) {arr[x] = v; return;}
    int m = (lx+rx)/2;
    if (i < m)
    {
      set(i,v,2*x+1,lx,m);
    }
    else{
      set(i,v,2*x+2,m , rx);
    }
    arr[x] = min(arr[2*x+1], arr[2*x+2]);
  }
  void set(int i, int v)
  {
    set(i,v,0,0,size);
  }

int query(int l , int r , int x, int lx , int rx)
{
  if (lx >= r || l >= rx) return INT_MAX;
  if (lx >= l && rx <= r) return arr[x];

  int m = (lx+rx)/2;
  int m1 = query(l,r,2*x+1,lx,m);
  int m2 = query(l,r,2*x+2,m,rx);
  return min(m1,m2);
}
  int query(int l , int r){
    return query(l,r,0,0,size);
  }

};
int main(){
  int n , m;
  cin >> n >> m;
  Segment st ;
  st.init(n);

  vector<int> a(n);
  for(int i = 0; i < n; i++)
  {
    cin >> a[i];
  }
  st.build(a);

  while (m--)
  {
    int t;
    cin >> t;
    if(t == 1)
    {
      int i ,v;
      cin >> i >> v;
      st.set(i,v);
    }
    else{
      int l , r;
      cin >> l >> r;
      int ans = st.query(l,r);
      cout << ans <<endl;
    }
  }
  

  return 0;
}