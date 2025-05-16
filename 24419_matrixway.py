import sys
import math
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
M = list(list(map(int, input().split())) for _ in range (N))

# 행렬 경로 재귀 호출
recursion_count = 0

def matrix_path_RC(M, N):
    global recursion_count
    recursion_count = 0
    matrix_path_rec(M, N-1, N-1)
    return recursion_count%1000000007
    

def matrix_path_rec(M, i, j):
    global recursion_count
    if i < 0 or j < 0:
        recursion_count += 1
        return 0
    else:
        return (M[i][j] + (max(matrix_path_rec(M, i - 1, j), matrix_path_rec(M, i, j - 1))))

print(matrix_path_RC(M, N))
# 그냥 규칙성 찾아서 런타임에러 방지하기
print((math.factorial(2 * N) // (math.factorial(N) ** 2))%1000000007)
# 행렬 경로 동적 프로그래밍
DP = 0

def matrix_path_DP(M, N):
    global DP
    DP = 0
    d = [[0]*(N+1) for _ in range (N+1)]
    for i in range (1, N+1):
        for j in range (1, N+1):
            d[i][j] = M[i-1][j-1] + (max(d[i-1][j], d[i][j-1]))
            DP += 1
    return DP%1000000007

print(matrix_path_DP(M, N))
