in_n = int(input())
paper_n = [list(map(int, input().split())) for _ in range(in_n)]
answer = [0] * 2


def cut_paper(para_n, para_x, para_y):
    # 종이 판별 과정
    color_wb = paper_n[para_x][para_y]
    for x in range(para_x, para_x + para_n):
        for y in range(para_y, para_y + para_n):
            if paper_n[x][y] != color_wb:
                cut_paper(para_n // 2, para_x, para_y)
                cut_paper(para_n // 2, para_x + para_n // 2, para_y)
                cut_paper(para_n // 2, para_x, para_y + para_n // 2)
                cut_paper(para_n // 2, para_x + para_n // 2, para_y + para_n // 2)
                return

    answer[color_wb] += 1


cut_paper(in_n, 0, 0)
for a in answer:
    print(a)
