from collections import deque

M, N = map(int, input().split())
Box = [list(map(int, input().split())) for _ in range(N)]
directions = [(-1,0), (1,0), (0,-1), (0,1)]

queue = deque()

for i in range(N):
    for j in range(M):
        if Box[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and Box[nx][ny] == 0:
            queue.append((nx, ny))
            Box[nx][ny] = Box[x][y] + 1
            
Result = max(map(max, Box))

for row in Box:
    if 0 in row: 
        print(-1)
        break
else:
    print(Result- 1)
