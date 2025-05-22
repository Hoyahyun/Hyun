N = int(input())
Time = []
Pay = []
Best = [0]* (N+1)

Time.append(0)
Pay.append(0)

for _ in range (N):
    T, P = map(int, input().split())
    Time.append(T)
    Pay.append(P)

for i in range (1,N+1):
    Best[i] = max(Best[i], Best[i-1]) # 보상 보존
    fin_date = i + Time[i] - 1
    if fin_date <= N:
        Best[fin_date] = max(Best[fin_date], Best[i-1]+Pay[i]) # 최대 보상 갱신
        
print(Best[N])
