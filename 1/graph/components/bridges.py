
def dfs(graph,tin,low,visited,timer,v,p=-1):
    visited[v] = True
    timer +=1
    tin[v] = low[v] = timer

    for to in graph[v]:
        if to == p:continue
        if visited[to]:
            low[v] = min(low[v], tin[to])
        else:
            dfs(graph,tin,low,visited,timer,to,v)
            low[v] = min(low[v],low[to])
            if low[to] > tin[v]:
                print(v,to)
    

        
def findBridge(graph, n):
    visited = [False]*(n+1)
    tin = [-1]*(n+1)
    low = [-1]*(n+1)
    timer = 0

    for i in range(1,n):
        if not visited[i]:
            dfs(graph,tin,low,visited,timer,i)
    
    



if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n,m = map(int, input().split())
        graph = [[] for _ in range(n+1)]

        while m >0:
            u,x = map(int, input().split())
            graph[u].append(x)
            graph[x].append(u)
            m -=1
        
        findBridge(graph,n)
        
        t -=1
