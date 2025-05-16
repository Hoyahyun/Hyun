import sys
sys.setrecursionlimit(int(1e5)) 
input = sys.stdin.readline

A = int(input())
array_a = list(map(int, input().split()))
array_b = list(map(int, input().split()))

def quick_sort(array, low, high, compare):
    if low < high:
        pivot = partition(array, low, high, compare)
        quick_sort(array, low, pivot - 1, compare)
        quick_sort(array, pivot + 1, high, compare)
    
    
def partition(array, low, high, compare):
    pivot = array[high]
    i = low - 1
    for j in range(low, high): 
        if array[j] <= pivot:
            i += 1  
            array[i], array[j] = array[j], array[i]
        if array[j] == compare[j]:
            if compare == array:
                print(1)
                exit(0)
    if i + 1 != high:
        array[i + 1], array[high] = array[high], array[i + 1]
    if array[i+1] == compare[i+1]:
        if compare == array:
            print(1)
            exit(0)
    return i + 1

if array_a == array_b:
    print(1)
    exit(0)    
quick_sort(array_a, 0, A - 1, array_b)
print(0)
