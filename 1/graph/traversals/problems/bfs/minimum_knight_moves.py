
graph = [[0 for _ in range(8)] for _ in range(8)]
dx = [-2,-1,1,2,2,1,-1,-2]
dy = [-1,-2,-2,-1,1,2,2,1]

def check(visited,x,y):
    if x < 0 or  x>7 or y < 0 or y > 7: return False
    if visited[x][y]: return False
    return True 

def bfs(x1,y1,x2,y2):
    flag = 0

    visited = [[False for _ in range(8)] for _ in range(8)]
    q = []
    q.append((x1,y1))
    dist = [[-1 for _ in range(8)] for _ in range(8)]
    visited[x1][y1] = True
    dist[x1][y1] = 0

    while q and flag == 0:
        u,v = q.pop(0)
        visited[u][v] = True
        if u == x2 and v == y2:
            flag = 1
            break

        for i in range(8):
            u1 = u + dx[i]
            v1 = v + dy[i]

            if check(visited,u1,v1):
                visited[u1][v1] = True
                dist[u1][v1] = dist[u][v]+1
                q.append((u1,v1))
    print(dist[x2][y2])
    



if __name__ == "__main__":

    t = int(input())
    while t > 0:
        x,y = input().split()
        x = list(x)
        y = list(y)
        x1 = ord(x[0]) - ord('a')
        y1 = int(x[1]) - 1

        x2 = ord(y[0]) - ord('a')
        y2 = int(y[1]) -1

        bfs(x1,y1,x2,y2)
        




        t -=1

