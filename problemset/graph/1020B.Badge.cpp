#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n ;
    cin >> n;

    vector<int> graph[n+1];

    for(int i=1; i<n+1; i++)
    {
        int a;
        cin >> a;
        graph[i].push_back(a);
    }

    queue<int> bfs;
    bool visited[n+1] = {false};
    bfs.push(1);
  

    for(int i=1; i<n+1; i++)
    {
        bfs.pop();
        bfs.push(i);
        visited[n+1] = {false};
        while (!bfs.empty())
        {
            
        
        int temp = bfs.front();
        if(visited[temp] == true)
        {
            cout << temp << " ";
            break;
        }

        visited[temp] = true;
        bfs.pop();
        bfs.push(graph[temp][0]);
        
        }
       

    }
    





    return 0;
}