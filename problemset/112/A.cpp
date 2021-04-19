#include <bits/stdc++.h>

using namespace std;


int main()
{

  string a,b;
  cin >> a ;
  cin >> b;
  int len = a.length();
  int result;

  for(int i=0; i<len;i++)
  {
     if(tolower(a[i]) == tolower(b[i]))
     result = 0;
     else if(tolower(a[i]) > tolower(b[i]))
     {
     result = 1;
     break;
     }
     else if(tolower(a[i]) < tolower(b[i]))
     {
     result = -1;
     break;
     }

  }
  cout << result;


    return 0;
}