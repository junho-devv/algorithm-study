def solution():
    # 테스트 케이스의 개수(num_t) 입력받기
    num_t = int(input())

    for _ in range(num_t):
        # 호텔의 높이(height_x), 너비(width_x), N번째 손님(guest_x) 입력받기
        height_x, width_x, guest_x = map(int, input().split())

        if guest_x % height_x == 0:
            floor_x = guest_x // height_x
            rest_x = height_x

        else:
            floor_x = guest_x // height_x + 1
            rest_x = guest_x % height_x

        answer = str(rest_x) + str(floor_x).zfill(2)
        print(answer)


solution()
