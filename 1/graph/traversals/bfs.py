def bfs(graph,n):
    queue = []
    visited = [False]*(n+1)
    queue.append(1)
    visited[1] = True

    while queue:
        x = queue.pop(0)
        print(x, end = "->")
        
        for i in graph[x]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

if __name__ == "__main__":
    n = int(input())
    t = n
    graph = [[] for _ in range(n+1)]
    while n -1>0:
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
        n -=1

    bfs(graph,t)
