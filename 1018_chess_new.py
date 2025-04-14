N, M = map(int, input().split())

board = []
num_sum = []

# 2차원 배열로 받기
for i in range (N):
    board.append(list(input().strip()))
    
# 각 값을 아스키 코드를 이용해서 B는 0, W는 1로 바꿔주기
for row in range(len(board)):
    for color in range(len(board[row])):
        board[row][color] = (ord(board[row][color]) % 2)

# 각 값에 대해서 전부 순회하면서 값 더해주고, 64에서 빼준 값 중에 min 값 찾기
for i in range (N-7):
    for j in range (M-7):
        number = 0
        for k in range (i, i+8):
            for l in range (j, j+8):
                board_num = (k + l + board[k][l]) % 2
                number = number + board_num
        num_sum.append(min(number, 64-number))

# 8 * 8 배열 여러개 중에서도 최소값 찾기
print(min(num_sum))
