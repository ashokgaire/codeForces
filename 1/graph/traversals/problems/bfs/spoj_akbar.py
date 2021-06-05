if __name__ == "__main__":
    t = int(input())

    while t > 0:
        n , r, m = map(int, input().split())
        graph = [[] for _ in range(n+1)]
        while r > 0:
            u , v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
            r -=1

        flag = 0
        ans = [None]*(n+1)
        visited = [False]*(n+1)
        level = [0] * (n+1)

        while m > 0:
            sr,x = map(int, input().split())
            q = []
            q.append(sr)
            visited[sr] = True

            if ans[sr]:
                flag = 1
            else:
                ans[sr] = 1
                level[sr] = 0
                while  flag == 0 and q:
                    u = q.pop(0)
                    visited[u] = True

                    for item in graph[u]:
                        if visited[item] == False:
                            visited[item] = True
                            level[item] = level[u] + 1
                            if level[item] <= x:
                                q.append(item)
                                if ans[item]:
                                    flag = 1
                                    break
                                else:
                                    ans[item] = 1
            m -=1
        for i in range(1,n+1):
            if ans[i] == 0:
                flag = 1
                break
        
        if flag == 1:
            print("No")
        else:
            print("Yes")
        
        t -=1
