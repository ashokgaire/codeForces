#include <bits/stdc++.h>

using namespace std;


int main()
{

   int n,k;
   cin >> n >> k;
   vector<int> a;
   while (n--)
   {
       int v;
       cin >> v;
       a.push_back(v);
   }

   int result = 0;
  
   for(int i=0; i<a.size(); i++)
   {
      

       if(a[i] >= a[k-1] && a[i]> 0)
       {
           result +=1;
       } 
   }
    cout << result;
   


    return 0;
}