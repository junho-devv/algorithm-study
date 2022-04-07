import sys


def solution():
    MAX = int(1e9)

    size_n, size_m = map(int, sys.stdin.readline().split())

    board_nm = []
    for _ in range(size_n):
        board_nm.append(str(sys.stdin.readline()))

    black_board = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
    white_board = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']

    min_nm = MAX

    for a in range(0, size_n - 8 + 1):
        for b in range(0, size_m - 8 + 1):
            count_b = 0
            count_w = 0

            for c in range(0, 8):
                for d in range(0, 8):
                    if black_board[c][d] != board_nm[a + c][b + d]:
                        count_b += 1

                    if white_board[c][d] != board_nm[a + c][b + d]:
                        count_w += 1

            min_nm = min(min_nm, min(count_w, count_b))

    print(min_nm)


solution()
