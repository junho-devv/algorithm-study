import sys

input = sys.stdin.readline


def dist(para_dot_1, para_dot_2):
    return (para_dot_1[0] - para_dot_2[0]) ** 2 + (para_dot_1[1] - para_dot_2[1]) ** 2


def solve(para_set, para_n):
    # 점이 두 개일때, 두점 거리만 구하면 됩니다.
    if para_n == 2:
        return dist(para_set[0], para_set[1])
    # 점이 세 개일때는 각 두점 사이의 거리를 구해서 최솟값을 구하면 됩니다.
    elif para_n == 3:
        return min(dist(para_set[0], para_set[1]), dist(para_set[1], para_set[2]), dist(para_set[0], para_set[2]))

    mid_x = (para_set[in_n // 2 - 1][0] + para_set[in_n // 2][0]) // 2
    # x축을 기준으로 짧은 거리 d를 구합니다.
    dist_x = min(solve(para_set[:para_n // 2], para_n // 2), solve(para_set[para_n // 2:], para_n // 2))

    # x 축 기준을 잊지 말것
    # 유효 거리 d보다 짧거나 같은 것을 제외하고 나머지는 제외시킵니다.
    # 즉, 두점 거리가 d보다 먼 경우는 제외합니다.
    short_check = []
    for dot in para_set:
        if dist_x >= (mid_x - dot[0]) ** 2:
            short_check.append(dot)
    short_check.sort(key=lambda x: x[1])

    if len(short_check) == 1:
        return dist_x
    else:
        dist_y = dist_x

        # x축만 고려하면 아직 고려해야할 점의 개수가 많이 남아있어 시간초과가 뜨게 됩니다.
        # 따라서 y축을 고려해주어 y축 기준의 d보다 긴 경우는 전부 제외시켜 주어야 합니다.
        # 세 가지 경우는 필수로 제외합니다.
        for i in range(len(short_check) - 1):
            for j in range(i + 1, len(short_check)):
                # y축 기준, 기본적으로 최소 길이 d보다 사이 거리가 긴 경우 제외
                if dist_x < (short_check[i][1] - short_check[j][1]) ** 2:
                    break
                # 두 점 모두 왼쪽에 있는 경우
                elif short_check[i][0] < mid_x and short_check[j][0] < mid_x:
                    continue
                # 두 점 모두 오른쪽에 있는 경우
                # 두 점이 mid를 지나는 점과 비교해보세요
                elif short_check[i][0] > mid_x and short_check[j][0] > mid_x:
                    continue

                dist_y = min(dist_y, dist(short_check[i], short_check[j]))

    return dist_y


in_n = int(input())
list_xy = [list(map(int, input().split())) for _ in range(in_n)]
# 2차원 리스트를 set 으로 변환시키기
set_xy = list(set(map(tuple, list_xy)))
# 좌표가 같은 두 점 사이의 거리는 0
if len(set_xy) != len(list_xy):
    print("0")
else:
    set_xy.sort()
    print(solve(set_xy, in_n))
