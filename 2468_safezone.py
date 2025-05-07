from collections import deque

N = int(input())
region = [list(map(int, input().split())) for _ in range(N)]
MAX_LEVEL = max(map(max, region))
directions = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs(x, y, safe, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and safe[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

result = 0
for h in range(MAX_LEVEL + 1):
    safe = [[region[i][j] > h for j in range(N)] for i in range(N)]
    visited = [[False]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if safe[i][j] and not visited[i][j]:
                bfs(i, j, safe, visited)
                count += 1
    result = max(result, count)

print(result)
