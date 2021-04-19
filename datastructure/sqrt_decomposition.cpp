#include <bits/stdc++.h>

using namespace std;


#define MAXN 10000
#define SQRTSIZE 100

int arr[MAXN];
int block[SQRTSIZE];
int blk_SZ;


// O(1)
void update(int idx, int val)
{
    int blocknumber = idx / blk_SZ;
    block[blocknumber] += val - arr[idx];
    arr[idx] = val;
}

// O(sqrt(n))
int query(int l, int r)
{
    int sum = 0;
    while(l < r and l%blk_SZ and l!=0)
    {
        sum += arr[l];
        l++;
    }
    while(l+blk_SZ <=r)
    {
        sum += arr[l];
        l++;
    }
    return sum;
}

void preprocess(int input[], int n)
{
    // init block pointer
    int blk_idx =-1;

    // calculate the  size of block 
    blk_SZ = sqrt(n);

    // building the decomposed array

    for(int i=0; i<n; i++)
    {
        arr[i] = input[i];
        if(i%blk_SZ == 0)
        {
            //entering next block 
            // incrementing block pointer
            blk_idx++;

        }
        block[blk_idx] += arr[i];
    }

}
int main()
{
    // We have used separate array for input because
    // the purpose of this code is to explain SQRT
    // decomposition in competitive programming where
    // we have multiple inputs.
    int input[] = {1, 5, 2, 4, 6, 1, 3, 5, 7, 10};
    int n = sizeof(input)/sizeof(input[0]);
  
    preprocess(input, n);
  
    cout << "query(3,8) : " << query(3, 8) << endl;
    cout << "query(1,6) : " << query(1, 6) << endl;
    update(8, 0);
    cout << "query(8,8) : " << query(8, 8) << endl;
    return 0;
}