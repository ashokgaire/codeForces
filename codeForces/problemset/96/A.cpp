#include <bits/stdc++.h>


using namespace std;


int main()
{

 string a;
 cin >> a;
 auto curr = a[0];
 int count = 1;
 vector<int> total;


  for(int i=1; i<a.size()+1;i++)
  {
     if(a[i] == curr) 
     {count++;
     curr = a[i];
     }
     else{
         total.push_back(count);
         count = 1;
         curr = a[i];
     }

  }


  int ans =  *max_element(total.begin(),total.end());

  if (ans >=7 )
{
    cout << "YES";
}
else{
    cout << "NO";
}
 
 return 0;
}
