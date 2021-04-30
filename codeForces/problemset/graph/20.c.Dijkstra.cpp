#include <bits/stdc++.h>

using namespace std;

const int INF = 1000000000;
vector<vector<pair<int, int>>> adj;

void dijkstra(int s, vector<int> & dist, vector<int> & pair)
{
    int n = adj.size();
    dist.assign(n , INF);
    pair.assign(n,-1);

    vector<bool> u(n,false);

    dist[s] = 0;

    for(int i=0; i < n; i++)
    {
        int v =-1;
        z

    }
}
int main()

{
    int n, m;
    cin >> n >> m;
    while (m--)
    {
        int a,b,w;
        cin  >> a >> b >> w;
        adj[a].push_back({b,w});
    }
    


    return 0;
}