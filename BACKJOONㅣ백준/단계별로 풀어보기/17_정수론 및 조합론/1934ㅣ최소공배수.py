import sys
input = sys.stdin.readline


def gcd(para_a, para_b):
    return gcd(para_b, para_a % para_b) if para_b else para_a


def lcm(para_a, para_b):
    return para_a * para_b // gcd(para_a, para_b)


num_tc = int(input())
for tc in range(num_tc):
    int_a, int_b = map(int, input().split())
    print(lcm(int_a, int_b))
