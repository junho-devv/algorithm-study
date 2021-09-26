import sys


input = sys.stdin.readline

in_n = int(input())
paper_n = [list(map(int, input().split())) for _ in range(in_n)]


def cut_paper(para_n, para_x, para_y):
    check_n = paper_n[para_x][para_y]
    for x in range(para_x, para_x + para_n):
        for y in range(para_y, para_y + para_n):
            if paper_n[x][y] != check_n:
                cut_paper(para_n // 3, para_x, para_y)
                cut_paper(para_n // 3, para_x, para_y + para_n // 3)
                cut_paper(para_n // 3, para_x, para_y + para_n // 3 * 2)

                cut_paper(para_n // 3, para_x + para_n // 3, )