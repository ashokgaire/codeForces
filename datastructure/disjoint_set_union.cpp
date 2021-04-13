#include <bits/stdc++.h>

#define MAXN 100000

using namespace std;

int parent[MAXN], rnk[MAXN],N;
bool rm[MAXN];


int getParent(int x)
{
    if(parent[x] == x) return x;
    parent[x] = getParent(parent[x]);
    return parent[x];
}

int uniteParent(int x, int y)
{
    int p1= getParent(x) , p2 = getParent(y);

    if(rnk[p1] > rnk[p2])
    {
        parent[p2] = p1;
        rnk[p1] = rnk[p2] +1;
    }
    else
    {
        parent[p1] = p2;
        rnk[p2] = max(rnk[p2],rnk[p1]+1);
    }
}

void disunion(int nroot)
{
    int p;

    for(int i=0; i<N;++i) getParent(i);
    for(int i=0; i<N; ++i)
    {
        p = getParent(i);
        if(rm[p] && !rm[i])
        {
            parent[p] = i;
            parent[i] = i;
        }
    }

    for(int i=0;i<N;++i) getParent(i);
    for(int i=0;i<N;++i)
    {
        if(rm[i])
        {
            parent[i] = nroot;
            rm[i] = 0;
        }
    }

    memset(rnk,0,sizeof(rnk));
    for(int i=0;i<N;++i)
    {
        p = getParent(i);
        if(p!=i)
        rnk[p] = 1;
    }
}