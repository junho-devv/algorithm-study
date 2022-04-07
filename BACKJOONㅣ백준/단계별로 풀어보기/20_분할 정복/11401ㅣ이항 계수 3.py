import sys


input = sys.stdin.readline

in_n, in_k = map(int, input().split())


def power(para_a, para_b):
    if para_b == 0:
        return 1

    if para_b % 2:
        return (power(para_a, para_b // 2) ** 2 * para_a) % pn
    else:
        return (power(para_a, para_b // 2) ** 2) % pn


# 소수(pn, prime number)
pn = int(1e9) + 7
# 모듈러 연산 분배법칙에 의해 연산을 할 때마다 %pn 해주기
list_factorial = [1 for _ in range(in_n + 1)]
for i in range(2, in_n + 1):
    list_factorial[i] = (list_factorial[i - 1] * i) % pn

val_a = list_factorial[in_n]
val_b = (list_factorial[in_n - in_k] * list_factorial[in_k]) % pn
# 페르마 소정리에 의해 결과는,
answer = (val_a * power(val_b, pn-2)) % pn
print(answer)

# 페르마의 소정리
# (A / B) % p
# = (A * B^-1) % p
# = A * B^-1 * B^p-1 % p
# = A * B^p-2 % p
# = (A % p) * (B^p-2 % p) % p
