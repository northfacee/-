N = int(input())
graph = [input() for i in range(N)]

answer= []
color = ['R','G','B']
def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if graph_1[x][y] == k:
        graph_1[x][y] = 0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

graph_1 = []
for i in graph:
    graph_1.append(list(i))
    
result = 0
for i in range(N):
    for j in range(N):
        for k in color:
            if dfs(i,j) == True:
                result +=1
answer.append(result)

graph_1 = []
for i in graph:
    graph_1.append(list(i))
    
result =0

for i in range(N):
    for j in range(N):
        if graph_1[i][j] == 'G':
            graph_1[i][j] = 'R'

for i in range(N):
    for j in range(N):
        for k in color:
            if dfs(i,j) == True:
                result +=1
answer.append(result)

print(*answer, sep=' ')
