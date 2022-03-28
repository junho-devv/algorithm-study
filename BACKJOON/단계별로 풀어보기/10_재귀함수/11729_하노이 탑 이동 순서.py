import sys


def move_the_hanoi_tower(x_disk, a_pole, b_pole, c_pole):

    if x_disk == 1:
        print(a_pole, c_pole)

    else:
        move_the_hanoi_tower(x_disk - 1, a_pole, c_pole, b_pole)
        print(a_pole, c_pole)
        move_the_hanoi_tower(x_disk - 1, b_pole, a_pole, c_pole)


def solution():
    # 원판의 개수(dist_x) 입력받기
    disk_x = int(input())
    in_x = int(sys.stdin.readline())
    print(2 ** in_x - 1)

    move_the_hanoi_tower(in_x, 1, 2, 3)


solution()
