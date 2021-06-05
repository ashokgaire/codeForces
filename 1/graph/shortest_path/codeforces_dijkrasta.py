import heapq


def dijkastra(graph,par, s,t,n):
    visited = [False]*(n+1)
    dist = [float('infinity')]*(n+1)
    dist[s]  = 0
    par[s] = -1
    pq = [(0,s)]

    while pq:
        current_distance, u = heapq.heappop(pq)

        if u == t: return True
        visited[u] = True

        for v , w  in graph[u]:
            if visited[v] == False and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                par[v] = u
                heapq.heappush(pq,(dist[v], v))
    return False
    

    


if __name__ == "__main__":
    n , m = map(int,input().split())
    graph =  [[] for _ in range(n+1)]

    while m > 0:
        u,v,c = map(int, input().split())
        graph[u].append((v,c))
        graph[v].append((u,c))
        m -=1 
    
    par = [None]*(n+1)
    if dijkastra(graph, par,1,n,n):
        path = []
        v = n
        
        while  v !=-1:
            v = par[v]
            if v != -1:
                path.append(v)
        
        for i in range(len(path)-1,-1, -1):
            print(path[i], end= " ")
        print(n)
    else:
        print(-1)
    