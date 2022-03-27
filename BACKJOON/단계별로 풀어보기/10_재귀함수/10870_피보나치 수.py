import sys


def do_fibonacci(a_num):

    if a_num == 0:
        return 0

    elif a_num == 1:
        return 1

    else:
        return do_fibonacci(a_num - 1) + do_fibonacci(a_num - 2)


if __name__ == '__main__':
    in_x = int(sys.stdin.readline())

    out_1 = do_fibonacci(in_x)
    print(out_1)
