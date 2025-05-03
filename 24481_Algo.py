import sys
sys.setrecursionlimit(10**)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    for i in sorted(graph[v]):
        if visited[i] == -1:
            visited[i] = visited[v]+1
            dfs(i)
            
visited[r] = 0
dfs(r)
for i in range(1, n + 1):
    print(visited[i])
