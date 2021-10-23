import sys


in_w, list_w = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split()))
in_m, list_m = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split()))
# 저울 왼쪽 추 무게와 오른쪽 추 무게의 차이를 저장할 리스트(diff_lr)
diff_lr = [False] * 40001
# table_dp[a][b] = a번째 추를 올리기 전, 양쪽 추의 무게차이 b
table_dp = [[0] * 15001 for _ in range(in_w + 1)]


def scale(para_num, para_left, para_right):
    temp_diff = abs(para_left - para_right)
    if not diff_lr[temp_diff]:
        diff_lr[temp_diff] = True

    if para_num == in_w:
        return

    if table_dp[para_num][temp_diff] == 0:
        scale(para_num + 1, para_left, para_right)
        scale(para_num + 1, para_left + list_w[para_num], para_right)
        scale(para_num + 1, para_left, para_right + list_w[para_num])

        table_dp[para_num][temp_diff] = 1


scale(0, 0, 0)

for m in list_m:
    if diff_lr[m]:
        print("Y", end=' ')
    else:
        print("N", end=' ')
