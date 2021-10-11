import sys

input = sys.stdin.readline


def is_prime_number(para_n):
    for m in range(2, int(para_n ** 0.5) + 1):
        if para_n % m == 0:
            return False
    else:
        return True


in_n = int(input())
table_dp = [[] for _ in range(in_n + 1)]
table_dp[1] = [2, 3, 5, 7]
for n in range(2, in_n + 1):
    for one in table_dp[n - 1]:
        for k in range(1, 10, 2):
            temp_int = one * 10 + k
            if is_prime_number(temp_int):
                table_dp[n].append(temp_int)

for ans in table_dp[in_n]:
    print(ans)
