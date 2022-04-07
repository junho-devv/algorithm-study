def check(para_queen):

    for i in range(para_queen):
        if chess_board[para_queen] == chess_board[i] \
                or abs(chess_board[para_queen] - chess_board[i]) == para_queen - i:
            return False
    return True


def track(para_queen):

    global result

    if para_queen == N:
        result += 1

    else:
        for i in range(N):
            chess_board[para_queen] = i

            if check(para_queen):
                track(para_queen + 1)


N = int(input())

chess_board = [0] * N
result = 0

track(0)

print(result)
