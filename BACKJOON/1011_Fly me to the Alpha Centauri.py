def solution():
    # 테스트 케이스의 개수(num_t) 입력받기
    num_t = int(input())
    for _ in range(num_t):
        # 현재 위치 x(pos_x), 목표 위치 y(pos_y) 입력받기
        pos_x, pos_y = map(int, input().split())
        # 현재 위치에서 목표 위치까지 거리(dist_xy)
        dist_xy = pos_y - pos_x

        k = 0
        move_k = 1

        while dist_xy > move_k:
            k += 1
            move_k += k

        print(k + 1)


solution()
