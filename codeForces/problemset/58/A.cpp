#include <bits/stdc++.h>

using namespace std;

int main()
{
 string s;
 cin >> s;
 string match = "hello";
 int i = 0;

    for (int j=0; j< s.length(); j++)
    {
        if(i >= 5)
        {
            break;
        }
        if(s[j] == match[i])
        {
            i++;
        }


    }


if(i == 5)
{
    cout << "YES";
}
else
{
    cout << "NO";
}

return 0;
}