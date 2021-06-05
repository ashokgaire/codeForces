

if __name__ == "__main__":
    n,m,k = map(int, input().split())
    graph = [[]for _ in range(n+1)]
    forbidden = [0 for _ in range(n+1)]

    while m > 0:
        u,v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        m -=1
    while  k > 0:
        a,b,c = map(int, input().split())
        forbidden[a] = 1
        forbidden[b] = 1
        forbidden[c] = 1
        k -=1