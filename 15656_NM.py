N, M = map(int, input().split())

Number = list(map(int, input().split()))
Number.sort()
number = []

def dfs():
    if len(number) == M:
        print(' '.join(map(str,number)))
        return
    
    for i in Number:
        number.append(i)
        dfs()
        number.pop()

dfs()
