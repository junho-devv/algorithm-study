import sys


def move_the_hanoi_tower(para_disk, para_pole_1, para_pole_2, para_pole_3):

    if para_disk == 1:
        print(para_pole_1, para_pole_3)

    else:
        move_the_hanoi_tower(para_disk - 1, para_pole_1, para_pole_3, para_pole_2)
        print(para_pole_1, para_pole_3)
        move_the_hanoi_tower(para_disk - 1, para_pole_2, para_pole_1, para_pole_3)


def solution():
    in_x = int(sys.stdin.readline())

    out_1 = 2 ** in_x - 1
    print(out_1)

    move_the_hanoi_tower(in_x, 1, 2, 3)


solution()
