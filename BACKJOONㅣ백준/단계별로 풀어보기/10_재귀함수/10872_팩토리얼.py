import sys


def do_factorial(a_num):

    if a_num == 0:
        return 1

    return a_num * do_factorial(a_num - 1)


if __name__ == '__main__':
    in_x = int(sys.stdin.readline())

    out_1 = do_factorial(in_x)
    print(out_1)
