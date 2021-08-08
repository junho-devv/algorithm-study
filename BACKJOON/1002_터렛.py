import sys
from math import sqrt


# 테스트 케이스(num_tc)의 개수 입력받기
num_tc = int(sys.stdin.readline())

for _ in range(num_tc):
    joe_x, joe_y, joe_r, back_x, back_y, back_r = map(int, sys.stdin.readline().split())

    # 조규현-백승환 둘 사이의 거리(diff_jb) 계산하기
    diff_jb = sqrt((joe_x - back_x) ** 2 + (joe_y - back_y) ** 2)

    # 둘의 위치가 같고 둘이 계산한 상대편의 거리가 서로 같을 때,
    if diff_jb == 0 and joe_r == back_r:
        # 류재명이 있을 수 있는 위치의 개수가 무한대인 경우, '-1' 출력하기
        print(-1)

    # 두 원이 내접인 경우,
    elif diff_jb < max(joe_r, back_r):
        # 두 원의 접점이 두개일 때,
        if diff_jb + min(joe_r, back_r) > max(joe_r, back_r):
            print(2)
        # 두 원의 접점이 하나일 때,
        elif diff_jb == abs(joe_r - back_r):
            print(1)
        # 두 원의 접점이 없을 때,
        else:
            print(0)
    # 두 원이 외접인 경우,
    elif diff_jb >= max(joe_r, back_r):
        # 두 원의 접점이 두개일 때,
        if diff_jb < joe_r + back_r:
            print(2)
        elif diff_jb == joe_r + back_r:
            print(1)
        else:
            print(0)
