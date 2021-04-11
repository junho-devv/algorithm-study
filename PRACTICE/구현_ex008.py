# 외벽 점검

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


print("answer : ", solution())


# def find_start_point():
#
#     w_len = len(weak_list)
#
#     min_dist = int(1e9)
#
#     for i in range(w_len):
#
#         i_next = i + w_len - 1
#
#         value = abs(weak_list[i] - weak_list[i_next % w_len] - (i_next // w_len) * wall_length)
#
#         if min_dist > value:
#             min_dist = value
#             start_point = i
#
#     return start_point


# def solution():
#
#     answer = 0
#
#     w_len = len(weak_list)
#
#     start_point = find_start_point()
#     print(start_point)
#     weak_dist = 0
#
#     new_list = []
#
#     for i in range(w_len):
#         one = (start_point + i) % w_len
#         new_list.append(weak_list[one])
#
#     for i in range(w_len - 1):
#         print("1212")
#         temp = weak_dist
#
#         simple_dist = new_list[i + 1] - new_list[i]
#
#         if simple_dist < 0:
#             weak_dist += simple_dist + wall_length
#         else:
#             weak_dist += simple_dist
#
#         temp_list = [[0] * (len(dist_list))]
#
#         if max(dist_list) > weak_dist:
#             print("Aaa")
#             continue
#
#         for j in range(len(dist_list)):
#             print("bbbb")
#             if dist_list[j] > temp and temp_list == 0:
#                 temp_list[j] += 1
#                 weak_dist = 0
#                 answer += 1
#                 break
#
#     return answer
