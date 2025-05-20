import sys
input = sys.stdin.readline

N = int(input())
point = []
Best = []

for _ in range (N):
    point.append(int(input()))

if N == 1:
    print(point[0])
elif N == 2:
    print(point[1]+point[0])
else:
    Best.append(point[0])
    Best.append(point[1]+point[0])
    Best.append(max(point[0]+point[2], point[1]+point[2]))

    for i in range (3, N):
        Optimal = max(Best[i-3]+point[i-1]+point[i], Best[i-2]+point[i])
        Best.append(Optimal)

    print(Best[-1])
