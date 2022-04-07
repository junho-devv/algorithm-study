str_a = input()
str_b = input()

len_a = len(str_a)
len_b = len(str_b)

dynamic_str = [[0] * (len_b + 1) for _ in range(len_a + 1)]
# DP 테이블 초기화
for i in range(len_a + 1):
    dynamic_str[i][0] = i
for i in range(len_b + 1):
    dynamic_str[0][i] = i

for a in range(1, len_a + 1):
    for b in range(1, len_b + 1):
        if str_a[a - 1] == str_b[b - 1]:
            dynamic_str[a][b] = dynamic_str[a - 1][b - 1]
        else:
            dynamic_str[a][b] = 1 + min(dynamic_str[a][b - 1], dynamic_str[a - 1][b],
                                        dynamic_str[a - 1][b - 1])

print(dynamic_str[len_a][len_b])