#include <bits/stdc++.h>

using namespace std;

int main()
{
    string a;
    cin >> a;

    sort(a.begin() , a.end());
    a.erase(unique(a.begin(),a.end()), a.end());
    
    if(a.length() % 2 == 0)
    cout << "CHAT WITH HER!";
    else
    cout << "IGNORE HIM!";

    return 0;
}