from collections import deque  

F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range (F+1)]

def bfs():
    queue = deque()
    queue.append(S)
    
    visited[S] = 1
    
    while queue:
        x = queue.popleft()
        if x == G :
            return visited[x] - 1
        else:
            for y in (x+U,x-D):
                if 0 < y <= F and visited[y] == 0:
                    visited[y] = visited[x] + 1
                    queue.append(y)
    
    return "use the stairs"

print(bfs())

# 2번 풀이
F, S, G, U, D = map(int, input().split())

button = 0

while button < F and 0 < S <= F:
    if S == G:
        print(button)
        exit()
    if S > G and S > D or S < G and S + U > F:
        S -= D
    else:
        S += U
    button += 1

print("use the stairs")
