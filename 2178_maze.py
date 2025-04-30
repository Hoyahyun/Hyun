from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(N)]

def Maze(x, y):
    # Deque는 queue가 아니라 FIFO, LIFO 둘 다 가능함. 뒤에 popleft가 나오는 것도, FIFO로 만들어주기 위해서임.
    queue = deque()
    queue.append((x,y))
    
    # Queue가 남아있을때까지
    while queue:
        # FIFO
        x, y = queue.popleft()
        # 사방면 위치에 대해서 BFS 방법으로 탐색
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            # 1이라면 아직 방문하지 않은 노드라는 뜻
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1                
                
    return graph[N-1][M-1]

print(Maze(0,0))
