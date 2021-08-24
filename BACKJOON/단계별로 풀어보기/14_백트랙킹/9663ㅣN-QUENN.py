import sys


def solution():
    input_n = int(sys.stdin.readline())

    chess_board = [0] * input_n

    num_case = 0

    def check(para_queen):

        for i in range(para_queen):
            if chess_board[para_queen] == chess_board[i] or \
                    abs(chess_board[para_queen] - chess_board[i]) == para_queen - i:
                return False

        return True

    def track(para_queen):

        nonlocal num_case

        if para_queen == input_n:
            num_case += 1

        else:
            for i in range(input_n):
                chess_board[para_queen] = i
                if check(para_queen):
                    track(para_queen + 1)

    track(0)

    print(num_case)


solution()
