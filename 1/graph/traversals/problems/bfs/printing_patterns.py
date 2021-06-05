n = m = r = c = 0
dist = vist = [[]]

dx  = [0,-1,0,1,-1,-1,1,1]
dy =  [-1,0,1,0,-1,1,-1,1]
def isValid(x,y):
    if x < 0 or x > n-1 or y < 0 or y > m-1: return False
    if vis[x][y]: return False
    return True

def bfs(dist,vis):
    q = []
    vis[r][c] = True
    dist[r][c] = 0
    q.append((r,c))

    while q:
        x, y = q.pop(0)
        for i in range(8):
            xi = x+dx[i]
            yi = y + dy[i]

            if isValid(xi, yi):
                dist[xi][yi] = dist[x][y] + 1
                vis[xi][yi] = True
                q.append((xi, yi))

n, m , r, c = map(int, input().split())
dist = [[None for i in range(m)] for i in range(n)]
vis = [[False for i in range(m)] for i in range(n)]
bfs(dist, vis)

for i in range(n):
    for j in range(m):
        print(dist[i][j], end = " ")
    print()
