#include <bits/stdc++.h>

using namespace std;

int main()
{
int t;
cin >> t;

while(t--)
{
int a, b;
cin >> a >> b;

int result1  = a ^ (a&b);
int result2 = b ^ (a&b);
int result = result1+result2;
cout << result << endl;
}
    return 0;
}