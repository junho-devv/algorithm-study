# 외벽 점검

from itertools import permutations

# wall_length = int(input())
wall_length = 12
# weak_list = list(map(int, input().split()))
# dist_list = list(map(int, input().split()))

# weak_list = [1, 5, 6, 10]
# dist_list = [1, 2, 3, 4]

weak_list = [1, 3, 4, 9, 10]
dist_list = [3, 5, 7]


def calculate_left_dist(i):
    left_dist = weak_list[i] - weak_list[i - 1]
    if left_dist < 0:
        left_dist += wall_length

    return left_dist


def calculate_right_dist(i):

    w_len = len(weak_list)

    right_dist = weak_list[(i + 1) % w_len] - weak_list[i % w_len]

    if right_dist < 0:
        right_dist += wall_length

    return right_dist


def solution():

    answer = 0

    i = 0
    weak_dist = 0
    left_dist = 0
    right_dist = 0

    right_point = 0
    left_point = 0

    temp = weak_dist

    while len(weak_list) != 0:
        print("i", i)

        if i == 0:
            left_dist = calculate_left_dist(i)
            right_dist = calculate_right_dist(i)
            right_point = i + 1
            left_point = i - 1
            print(left_dist, right_dist, "+++++")
            print(right_point, left_point, "--------")

        if max(dist_list) > weak_dist:

            temp = weak_dist

            print(weak_list)
            print("weak distance", weak_dist)
            print("left, right distance", left_dist, right_dist)
            if left_dist < right_dist:
                print(1)
                weak_dist += left_dist
                i = left_point
                left_point -= 1
                left_dist = calculate_left_dist(i)

            else:
                print(2)
                weak_dist += right_dist
                i = right_point
                right_point += 1
                right_dist = calculate_right_dist(i)

            weak_list.remove(weak_list[i % len(weak_list)])

        else:

            for dist in dist_list:
                if dist >= temp:
                    answer += 1
                    dist_list.remove(dist)
                    weak_dist = 0
                    i = 0
                    break
            print("dist", dist_list)

    return answer


def solution_002(n, weak, dist):
    # 길이를 2배로 늘려서 원형을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # len(dist) + 1 투입할 친구 수의 최대값 + 1
    answer = len(dist) + 1
    # 0부터 length-1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            # 투입할 친구의 수
            count = 1
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]

            for index in range(start, start + length):

                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break

                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)

    if answer > len(dist):
        return -1

    return answer


print("answer : ", solution())
