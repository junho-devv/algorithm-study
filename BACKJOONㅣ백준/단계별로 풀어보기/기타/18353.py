# 병사의 수(s_num) 입력하기
s_num = int(input())
# 병사들의 전투력(p_list) 입력하기
p_list = list(map(int, input().split()))

dynamic_table = [1] * s_num
a_num = 1
a_power = int(1e9)

for i in range(1, s_num):
    for j in range(i):
        if p_list[i] < p_list[j]:
            dynamic_table[i] = max(dynamic_table[i], dynamic_table[j] + 1)

print(max(dynamic_table))
