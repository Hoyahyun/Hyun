import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

T = int(input())

def ancestor (baby, graph,parent):
    parent.append(baby)
    for i in range (len(graph)):
        if baby in graph[i]:
            parent.append(i)
            ancestor(i,graph,parent)
    return parent

total_parent = []

for _ in range (T):
    N = int(input())
    dfs_graph = [[] for _ in range (N+1)]
    for _ in range (N-1):
        A, B = map(int, input().split())
        dfs_graph[A].append(B)
    C, D = map(int, input().split())
    parent_C = []
    parent_D = []
    ancestor (C,dfs_graph,parent_C)
    ancestor (D,dfs_graph,parent_D)
    append = 0
    for k in range (len(parent_C)):
        for l in range (len(parent_D)):
            if parent_C[k] == parent_D[l]:
                total_parent.append(parent_C[k])
                append = 1
                break
        if append != 0:
            break
for m in range (len(total_parent)):
    print(total_parent[m])

# 수정 코드

import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    parent = [0] * (N + 1)

    for _ in range(N - 1):
        A, B = map(int, input().split())
        parent[B] = A  # B의 부모는 A로 기록

    C, D = map(int, input().split())

    # C의 모든 조상을 집합에 저장
    ancestors = set()
    while C:
        ancestors.add(C)
        C = parent[C]

    # D의 조상을 타고 올라가면서 C와 공통인 첫 조상을 찾음
    while D not in ancestors:
        D = parent[D]

    print(D)
