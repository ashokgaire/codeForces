#include <bits/stdc++.h>

using namespace std;

int main()
{ 
    int  x;
    cin >> x;
    int max = 5;
    int step = 0;
    int initial = 0;

    while(x > initial)
    {
        int temp = initial + max;
       
        if (temp <= x)
        {
            initial +=max;
            step +=1;
        }
        else
        {
            max -=1;
        }
    }

    cout << step ;


    return 0;
}