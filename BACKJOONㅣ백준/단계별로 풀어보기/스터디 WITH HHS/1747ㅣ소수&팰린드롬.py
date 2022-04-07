import sys


def is_prime_number(para_n):
    for i in range(2, int(para_n ** 0.5) + 1):
        if para_n % i == 0:
            return False
    else:
        return True


def find(para_max):
    while True:
        if str(para_max) == str(para_max)[::-1] and is_prime_number(para_max):
            return para_max
        else:
            para_max += 1


if __name__ == '__main__':
    MAX = int(1e6)

    in_n = int(sys.stdin.readline())

    out_min = 0
    for n in range(in_n, MAX + 1):
        if n == 1:
            continue

        if str(n) == str(n)[::-1] and is_prime_number(n):
            out_min = n
            break

    if out_min == 0:
        out_min = find(MAX)

    print(out_min)
