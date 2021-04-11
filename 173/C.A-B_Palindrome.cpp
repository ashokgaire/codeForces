#include <bits/stdc++.h>

using namespace std;


bool isPalndrome(char str[])
{
    int l =0;
    int h =  strlen(str) -1;

    while (h > l)
    {
        if (str[l++] != str[h--])
        {
            return false;
        }
    }
    return true;
    
}
int main()
{
    int n ;
    cin >> n;

    while (n--)
    {
        int a,b;
        cin >> a >> b;
        char arr[a+b];
        cin >> arr;
        int one,zero,wat = 0;

        for(int i=0; i<(a+b); i++)
        {
            if(arr[i] == '1')
             one++;
             if(arr[i] == '0')
             zero++;
             else
             wat++;
        }

     int l =0;
     int h =  (a+b) -1;

    while (h > l)
    {
        if (arr[l] != arr[h])
        {
            if(arr[l++] == '?')
            {
                if(zero >= 0){
                    arr[l++] == '0';
                    arr[h--] == '0';
                    zero--;
                }
                else if(one >=0){
                    arr[l++] =='1';
                    arr[h--] == '1';
                }
                
            }
            else{
                arr[h--] = arr[l++];
            }
        }
    }

   
        cout << arr << endl;
  

        

    }
    


    return 0;
}