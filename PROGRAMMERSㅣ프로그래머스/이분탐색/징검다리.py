def solution(distance, rocks, n):
    answer = 0

    rocks.append(distance)
    rocks.sort()

    rock_l, rock_r = 0, distance
    while rock_l < rock_r:
        rock_m = (rock_l + rock_r) // 2

        temp_rock, rock_remove = 0, 0
        for rock in rocks:
            temp_distance = rock - temp_rock
            if temp_distance < rock_m:
                rock_remove += 1
            else:
                temp_rock = rock

        if rock_remove > n:
            rock_r = rock_m - 1
        else:
            rock_l = rock_m + 1

    answer = rock_l

    return answer


if __name__ == '__main__':
    in_d = 25
    in_r = [2, 14, 11, 21, 17]
    in_n = 2

    solution(in_d, in_r, in_n)
