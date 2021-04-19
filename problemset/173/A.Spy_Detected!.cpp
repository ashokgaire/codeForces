#include <bits/stdc++.h>

using namespace std;


int findUnique(vector<int> a, int n)
{

   
    int count[1000];
    memset(count, 0, sizeof(count));


    for(int i = 0; i<=1000; i++)
        for(int j =0; j<n; j++)
            if(a[j]  == i)
               count[i] +=1;

    unsigned res = 0;
    for(int i=0; i <= 1000; i++)
        if(count[i] == 1)
           res = i;
    return res;
        
    

}


int main()
{
    int n ;
    cin >> n;

    while (n--)
    {
        int k ;
        cin >> k;
        vector<int> arr;
       
        
        for(int i=0;i<k;i++)
        {
            int num;
            cin >> num;
            
            arr.push_back(num);   
        } 
        int ans  = findUnique(arr, k);

        for(int i =0; i<k; i++)
        {
            if(arr[i] == ans)
            {
                cout << i+1 << endl;
            }
        }
    }
    


    return 0;
}