import sys


if __name__ == '__main__':
    in_n = list(map(int, sys.stdin.readline().split()))
    print(in_n)
    set_n = set(in_n)
    print(set_n)
    list_n = list(set_n)
    print(list_n)