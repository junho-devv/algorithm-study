import sys


def solution(n):
    answer = 0

    for x in range(2, n + 1):
        cnt = 0

        for y in range(1, x + 1):
            if x % y == 0:
                cnt += 1

        if cnt == 2:
            answer += 1

    return answer


def solution002():

    val = sys.stdin.readilne()
    row = int(val[1])
    col = int(ord(val[0])) - int(ord('a')) + 1

    # It stands for "ordinal".
    # The earliest use of ord that I remember was in Pascal.
    # There, ord() returned the ordinal value of its argument. 
    # For characters this was defined as the ASCII code.

    count = 0

    print(row, col)

    moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    for move in moves:
        n_row = row + move[1]
        n_col = col + move[0]

        if 0 < n_col < 9 and 0 < n_row < 9:
            count += 1

    print(count)


solution002()