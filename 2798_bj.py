# 입력 받기
N, M = map(int, input().split())

NUM = list(map(int, input().split()))

# 블랙잭 결과    
BJ = []

# 3중 for 문을 통해서 완전 탐색 진행 후, M 이하를 저장
for i in range (N-2):
    for j in range (i+1,N-1):
        for k in range (j+1,N):
            NUM_SUM = NUM[i]+NUM[j]+NUM[k]
            if NUM_SUM <= M:
                BJ.append(NUM_SUM)

print(max(BJ))
