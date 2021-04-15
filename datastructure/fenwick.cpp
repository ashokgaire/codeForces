#include <iostream>

using namespace std;

int getSum(int BITree[], int index)
{
    int sum = 0;
    index = index+1;

    while(index > 0)
    {
        sum += BITree[index];
        index -= index & (-index);
    }

return sum;
}

//updates a node in binary index tree at given index
//in BITree. the given value 'val' is added to BITree[i] and all of its ancestrs in tree
void updateBIT(int BITree[], int n, int index, int val)
{
    // index in BITree[] is 1 more than the index in arr[]
    index = index +1;

// Traverse all ancestors and add 'val'
    while (index <=n)
    {
        //add 'val' to current node of BI tree
        BITree[index] += val;

        //update index to that of parent in update view
        index += index & (-index);
    }
    
}


int *constructBITree(int arr[], int n)
{
    // create an initialize BITree as 0
    int *BITree = new int[n+1];
    for(int i=1; i<n; i++)
    {
        BITree[i] =0;
    }

    //store the actual values in BItree[] using update()
    for(int i=0; i<n; i++)
    {
        updateBIT(BITree,n,i,arr[i]);
    }

    return BITree;
}

int main()
{
    int freq[] = {2,1,1,3,2,3,4,5,6,7,8,9};
    int n = sizeof(freq) / sizeof(freq[0]);

    int *BITree = constructBITree(freq,n);

    freq[3] += 6;
    updateBIT(BITree, n, 3 , 6);

    cout << "\nSum of elements in arr[0..5] after update is "
        << getSum(BITree, 5);
  
    return 0;

}