def solution():

    row, col = int(in_n[1]) - 1, ord(in_n[0]) - ord('a')
    way_8 = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    answer = 0
    for way in way_8:
        next_row = row + way[0]
        next_col = col + way[1]

        if 0 <= next_row < 8 and 0 <= next_col < 8:
            answer += 1

    return answer


if __name__ == "__main__":

    import sys

    in_n = sys.stdin.readline()

    print(solution())
