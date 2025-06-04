def lotto(array, s, index, cnt):
    if cnt==6:
        print(*array)
        return
    
    for i in range(index, len(s)):
        array[cnt] = s[i]
        lotto(array, s, i+1, cnt+1)
    

while True:
    Number = list(map(int, input().split()))
    if Number[0]==0:
        break
    array = [0] * 6
    lotto(array, Number[1:], 0, 0)
    print()
