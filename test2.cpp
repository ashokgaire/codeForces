#include <bits/stdc++.h>
using namespace std;

int mergeSort(vector<int> arr, int n)
{
    vector<int> temparr(n,0);
    return _mergeSort(arr, temparr, 0,n-1);
}

int _mergeSort(vector<int> arr, vector<int> temparr, int left, int  right)
{
    int invcount = 0;

    if(left < right)
    {
        int mid = (left+right) / 2;
        invcount += _mergeSort(arr, temparr, left, mid);
        invcount += _mergeSort(arr, temparr, mid+1, right);

        invcount += merge(arr, temparr, left, mid, right);
    }

return invcount;

}

int merge(vector<int> arr, vector<int> temparr, int left, int mid, int right)
{
    int i = left ;
    int j = mid +1;
    int k = left;
    int invcount = 0;

    while(i <= mid && j <= right)
    {
        if (arr[i] <= arr[j])
        {
            temparr[k] = arr[i];
            k +=1;
            i +=1;

        }
        else{
            temparr[k] = arr[j];
            invcount += mid -i +1;
            k +=1;
            j +=1;

        }
    }

    while (i <= mid)
    {
        temparr[k] = arr[i];
        k +=1;
        i +=1;
    }

    while ( j <= right)
    {
        temparr[k] = arr[j];
        j +=1;
        k +=1;
    }

    for(int i = left; i <= right - 1; i++)
    {
        temparr[i] = arr[i];
    }

    return invcount;
    
}


int main()
{
    int n; 
    cin >> n;

    vector<int> arr(n,0);

    for(int i=0 ; i < n ; i ++)
    {
        int a;
        cin >> a;
        arr[i] = a;
    }
    int ans = mergeSort(arr, n);
    cout << ans;
}