#include <bits/stdc++.h>

using namespace std;


int main()
{

   int n,k;
   cin >> n >> k;
   
   int size = n*k;

   if(size % 2 == 0)
   {
       cout << size / 2;
   }
   else
   {
       cout << (size-1) /2;
   }



    return 0;
}