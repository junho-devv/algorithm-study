import sys


def move_the_hanoi_tower(para_disk, a_pole, b_pole, c_pole):

    if para_disk == 1:
        print(a_pole, c_pole)

    else:
        move_the_hanoi_tower(para_disk - 1, a_pole, c_pole, b_pole)
        print(a_pole, c_pole)
        move_the_hanoi_tower(para_disk - 1, b_pole, a_pole, c_pole)


def solution():
    in_x = int(sys.stdin.readline())
    print(2 ** in_x - 1)

    move_the_hanoi_tower(in_x, 1, 2, 3)


solution()
