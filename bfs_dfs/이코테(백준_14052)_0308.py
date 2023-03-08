from itertools import combinations
import copy
N,M = map(int, input().split())

labs = [list(map(int, input().split())) for i in range(N)]


# 벽 3개 넣을곳의 좌표를 먼저 넣어줌
w = []

for i in range(N):
    for j in range(M):
        if labs[i][j] == 0:
            w.append([i,j])

# 0 인 좌표 3개를 넣어줌
walls = []

for a in range(len(w)):
    for b in range(a+1,len(w)):
        for c in range(b+1, len(w)):
            walls.append([w[a],w[b],w[c]])

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    q = [(y,x)]
    while q:
        ey, ex = q.pop()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<= ny < N and 0<= nx <M:
                if graph[ny][nx] == 0 and chk[ny][nx]==False:
                    chk[ny][nx]= True
                    graph[ny][nx]=2
                    q.append((ny,nx))


max_point = 0
for wall in walls:
    graph = copy.deepcopy(labs)
    chk = [[False]*M for _ in range(N)]
    for wx,wy in wall: # 3개 벽 넣어줌
        graph[wx][wy] = 1

    for j in range(N):
        for i in range(M):
            if graph[j][i] == 2 and chk[j][i]==False:
                chk[j][i] == True
                dfs(j,i)
    safe_point = sum([row.count(0) for row in graph])
    max_point = max(safe_point, max_point)

print(max_point)
