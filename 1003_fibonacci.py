# 정석적인 피보나치 수열 풀이법
T = int(input())
Num = []

def fibonacci(N):
    global count_0
    global count_1
    if N == 0:
        count_0 += 1
        return 0
    elif N == 1:
        count_1 += 1
        return 1
    else:
        return fibonacci(N-1) + fibonacci(N-2)

for i in range (T):
    Num.append(int(input()))

for i in Num:
    count_0 = 0
    count_1 = 0
    fibonacci(i)
    print(count_0, count_1)
    
# 규칙성으로 풀기
# 1 0 / 0 1 / 1 1 / 1 2 / 2 3 / 3 5 / 5 8

for i in Num:
    count_0, count_1 = 1, 0
    for j in range (i):    
        count_0, count_1 = count_1, count_0 + count_1
    print(count_0, count_1)
