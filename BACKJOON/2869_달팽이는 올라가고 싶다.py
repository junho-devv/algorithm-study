def solution():

    dist_up, dist_down, height_x = map(int, input().split())

    dist_x = height_x - dist_up
    day_x = 1

    if dist_x > 0:
        day_y = dist_x // (dist_up - dist_down)
        day_x += day_y if day_y != 0 else 1

    answer = day_x
    # 결과(answer) 출력하기
    print(answer)


def solution_2():
    # 낮동안 올라간 거리(dist_up), 밤동안 내려간 거리(dist_down), 나무의 높이(height_v)
    dist_up, dist_down, height_v = map(int, input().split())
    # 높이 V를 올라가는데 걸리는 날짜
    day_v = (height_v - dist_up) / (dist_up - dist_down) + 1

    answer = int(day_v) if day_v == int(day_v) else int(day_v) + 1
    # 결과(answer) 출력하기
    print(answer)


solution_2()
