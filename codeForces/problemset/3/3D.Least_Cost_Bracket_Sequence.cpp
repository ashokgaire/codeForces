#include <bits/stdc++.h>

using namespace std;


int main(void)
{
    char str[50010];
    priority_queue<pair<long long, int>> pq;

    int num1=0, num2=0,a,b,flag=0;
    long long ans = 0;
    cin >> str;
    int len = strlen(str);
    for(int i=0; i<len; i++)
    {
        if(str[i] == '(')
        {
            num1++;
        }
        else if(str[i] == ')')
        {
            num2++;
        }
        else if(str[i] == '?')
        {
            cin >> a >> b;
            pq.push((make_pair(b-a,i)));
            str[i] = ')';
            ans +=b;
            num2++;
        }

        if(num2 > num1)
        {
            if(pq.empty())
            {
                flag=1;
                break;
            }

            pair<long long, int> t=pq.top();
            pq.pop();
            str[t.second] = '(';
            ans -= t.first;
            num1++;
            num2--;
        }


    }

    if(flag==1 || num1 !=num2)
    {
        cout << "-1\n";
    }
    else{
        cout << ans << endl;
        puts(str);
    }
return 0;
}