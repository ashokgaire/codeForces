    #include<bits/stdc++.h>
    using namespace std;
     
    int main()
    {
    	ios::sync_with_stdio(0);cin.tie(0);
    	mt19937 rng((unsigned int) chrono::steady_clock::now().time_since_epoch().count());
    	auto start=chrono::high_resolution_clock::now();
    	
    	//code here
        int n,t;
        cin >> n >> t;

        vector<int> graph[n+1];

        for(int i=1; i< n; i++)
        {
            int a;
            cin >> a;
            graph[i].push_back(a+i);
        }

        queue<int> bfs;
        bool visited[n+1] = {false};
        bfs.push(1);
        visited[1] = true;
        int fl= 0;

        while(!bfs.empty())
        {
            int temp = bfs.front();
            if(temp == t)
            {
                fl = 1;
                break;
            }

            bfs.pop();


            for(auto it=graph[temp].begin(); it!= graph[temp].end(); it++)
            {
                if(!visited[*it])
                {
                visited[*it] = true;
                bfs.push(*it);
                }
            }
        }

        if(fl == 1)
        {
            cout << "YES";
        }
        else
        {
            cout << "NO";
        }




     
    		
    	auto stop=chrono::high_resolution_clock::now();
    	auto duration=chrono::duration_cast<chrono::microseconds>(stop-start);
    	cerr<< endl << duration.count()/1000.0<<" ms\n";
    }