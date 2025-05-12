N, K = map(int, input().split())

array = list(map(int, input().split()))

count = 0

for i in range (N, 1,-1):
    for j in range (i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            count += 1
            if count == K:
                print(array[j], array[j+1])
                break
if count < K :
    print(-1)
