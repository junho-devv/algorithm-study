in_n = int(input())

list_m = []
for _ in range(in_n):
    list_m.append(int(input()))


def get_gcd(para_a, para_b):
    return get_gcd(para_b, para_a % para_b) if para_b else para_a

result_gcd =
for i in range(1, in_n):
    abs(list_m[i] - list_m[i - 1])
