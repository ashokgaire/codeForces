#  can use both dfs and bfs

def bfs(graph,visited,comp,node):
    q = []
    q.append(node)
    visited[node] = True

    while q:
        x = q.pop(0)
        visited[x] = True
        for v in graph[x]:
            if visited[v] == False:
                visited[v] = True
                q.append(v)
                comp.append(v)



def dfs(graph,visited,comp,node):
    visited[node] == True
    for ver in graph[node]:
        if visited[ver] == False:
            comp.append(ver)
            visited[ver] = True
            dfs(graph,visited,comp,ver)
    

def findComp(graph,n):
    visited = [False]*(n+1)
    comp = []
    ans = 0
    for i in range(1,n):
        if visited[i] == False:
            comp.clear()
            bfs(graph,visited,comp,1)
            ans +=1
        
    return ans
            



if __name__ == "__main__":
    n,m = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    while m >0:
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        m -=1
    
    ans = findComp(graph,n)
    print(ans)
