def solution():

    def check(para_x, para_y):

        list_19 = [n for n in range(1, 10)]

        for k in range(9):

            if sudoku_board[para_x][k] in list_19:
                list_19.remove(sudoku_board[para_x][k])

            if sudoku_board[k][para_y] in list_19:
                list_19.remove(sudoku_board[k][para_y])

        para_x //= 3
        para_y //= 3

        for x in range(para_x * 3, (para_x + 1) * 3):
            for y in range(para_y * 3, (para_y + 1) * 3):

                if sudoku_board[x][y] in list_19:
                    list_19.remove(sudoku_board[x][y])

        return list_19

    def depth_first_search(para_cnt_zero):

        nonlocal termination

        if termination:
            return

        if para_cnt_zero == len(list_zero):

            for row in sudoku_board:
                print(*row)

            termination = True
            return

        else:
            x, y = list_zero[para_cnt_zero]
            candidates = check(x, y)

            for candidate in candidates:
                sudoku_board[x][y] = candidate
                depth_first_search(para_cnt_zero + 1)
                sudoku_board[x][y] = 0

    list_zero = [(x, y) for x in range(9) for y in range(9) if sudoku_board[x][y] == 0]
    termination = False

    depth_first_search(0)


if __name__ == "__main__":

    import sys

    sudoku_board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

    solution()
