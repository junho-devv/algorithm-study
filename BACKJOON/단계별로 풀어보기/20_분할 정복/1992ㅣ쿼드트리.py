import sys


input = sys.stdin.readline

in_n = int(input())
display_n = [list(input().rstrip()) for _ in range(in_n)]
answer = ""


def compress_display(para_n, para_x, para_y):

    global answer

    check_01 = display_n[para_x][para_y]
    for x in range(para_x, para_x + para_n):
        for y in range(para_y, para_y + para_n):
            if display_n[x][y] != check_01:
                answer_1 = compress_display(para_n // 2, para_x, para_y)
                answer_2 = compress_display(para_n // 2, para_x, para_y + para_n // 2)
                answer_3 = compress_display(para_n // 2, para_x + para_n // 2, para_y)
                answer_4 = compress_display(para_n // 2, para_x + para_n // 2, para_y + para_n // 2)

                answer = "(" + answer_1 + answer_2 + answer_3 + answer_4 + ")"
                return answer

    return check_01


print(compress_display(in_n, 0, 0))

