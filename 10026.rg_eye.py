from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def is_same_color(c1, c2, is_color_weak):
    if is_color_weak:
        return (c1 in 'RG' and c2 in 'RG') or c1 == c2
    return c1 == c2

def bfs(x, y, visited, grid, is_color_weak):
    N = len(grid)
    queue = deque([(x, y)])
    visited[x][y] = True
    color = grid[x][y]

    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if is_same_color(color, grid[nx][ny], is_color_weak):
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def count_areas(grid, is_color_weak):
    N = len(grid)
    visited = [[False]*N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, visited, grid, is_color_weak)
                count += 1
    return count

# 입력
N = int(input())
grid = [list(input().strip()) for _ in range(N)]

# 출력
print(count_areas(grid, False), count_areas(grid, True))
