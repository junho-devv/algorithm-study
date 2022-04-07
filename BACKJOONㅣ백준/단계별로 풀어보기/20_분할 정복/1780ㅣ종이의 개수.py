import sys


input = sys.stdin.readline

in_n = int(input())
paper_n = [list(map(int, input().split())) for _ in range(in_n)]
answer = [0] * 3


def cut_paper(para_n, para_x, para_y):
    check_n = paper_n[para_x][para_y]
    for x in range(para_x, para_x + para_n):
        for y in range(para_y, para_y + para_n):

            if paper_n[x][y] != check_n:
                for x_n in [0, 1, 2]:
                    for y_n in [0, 1, 2]:
                        cut_paper(para_n // 3, para_x + para_n // 3 * x_n, para_y + para_n // 3 * y_n)
                return

    answer[check_n] += 1


cut_paper(in_n, 0, 0)

for i in [-1, 0, 1]:
    print(answer[i])
