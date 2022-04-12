from collections import deque

n, m = map(int, input().split())

circle = deque([i for i in range(1,n+1)])
result = []
while circle:
    for i in range(m):
        if i == m-1:
            left = circle.popleft()
            result.append(left)
        else:
            left = circle.popleft()
            circle.append(left)

print(f'<{str(result)[1:-1]}>')
