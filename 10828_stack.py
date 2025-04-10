import sys

N = int(input())
Stack = []

for i in range (N):
    Command = sys.stdin.readline().split()
    R_Command = Command[0]
    if R_Command == "push":
        Stack.append(Command[1])
    elif R_Command == "pop":
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack.pop())
    elif R_Command == "size":
        print(len(Stack))
    elif R_Command == "empty":
        if len(Stack) == 0:
            print(1)
        else:
            print(0)
    elif R_Command == "top":
        if len(Stack) == 0:
            print(-1)
        else:
            print(Stack[-1])
