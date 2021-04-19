#include <bits/stdc++.h>

using namespace std;

int main()
{
     int k, n, w;
     cin >> k >> n >> w;

     int result = 0;
     int j = 1;

     for(int i=0; i< w; i++)
     {
         result += k* j;
         j++;

     }

     if( result > n)
     cout << result - n;
     else
     cout << "0";



    return 0;
}