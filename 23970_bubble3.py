import sys
input = sys.stdin.readline

N = int(input())
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

def bubble(array_A, array_B):
    if array_A == array_B:
        print(1)
        return
    for i in range (N, 1,-1):
        for j in range (i-1):
            if array_A[j] > array_A[j+1]:
                array_A[j], array_A[j+1] = array_A[j+1], array_A[j]
                if array_A[j+1] == array_B[j+1]:
                    if array_A == array_B:
                        print(1)
                        return
    print(0)

bubble(array_A, array_B)
