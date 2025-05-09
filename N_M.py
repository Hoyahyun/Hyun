N, M = map(int, input().split())

number = []

def dfs():
    if len(number) == M:
        print(' '.join(map(str,number)))
        return
    
    for i in range (1, N+1):
        number.append(i)
        dfs()
        number.pop()

dfs()
