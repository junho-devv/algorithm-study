in_n = int(input())

list_m = []
for _ in range(in_n):
    list_m.append(int(input()))


def get_gcd(para_a, para_b):
    return get_gcd(para_b, para_a % para_b) if para_b else para_a


result_gcd = 0
for i in range(1, in_n):
    result_gcd = get_gcd(abs(list_m[i] - list_m[i - 1]), result_gcd)

result_factor = []
for i in range(1, int(result_gcd ** 0.5) + 1):
    if result_gcd % i == 0:
        result_factor.append(i)
        result_factor.append(result_gcd // i)

result_factor = list(set(result_factor))
result_factor.sort()

for i in range(1, len(result_factor)):
    print(result_factor[i], end=' ')
