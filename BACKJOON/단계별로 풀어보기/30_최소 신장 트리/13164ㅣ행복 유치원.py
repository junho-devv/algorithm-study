import sys


if __name__ == '__main__':
    in_n, in_k = map(int, sys.stdin.readline().split())
    list_kinder = list(map(int, sys.stdin.readline().split()))

    list_height = []
    for _ in range(in_n - 1):
        list_height.append(list_kinder[_ + 1] - list_kinder[_])
    list_height.sort()

    out_min = sum(list_height[:in_n - in_k])
    print(out_min)
