# 임의의 큰 수(INF) 설정하기
INF = int(1e9)
# 학생들의 수와 임의의 두 학생의 성적을 비교한 횟수 입력하기
num_s, num_c = map(int, input().split())
comparison_table = [[INF] * (num_s + 1) for _ in range(num_s + 1)]

for s_1 in range(1, num_s + 1):
    for s_2 in range(1, num_s + 1):
        if s_1 == s_2:
            comparison_table[s_1][s_2] = 0

for _ in range(num_c):
    student_1, student_2 = map(int, input().split())
    comparison_table[student_1][student_2] = 1

for s_1 in range(1, num_s + 1):
    for s_2 in range(1, num_s + 1):

        if comparison_table[s_1][s_2] == INF:
            print("E", end=" ")
        else:
            print(comparison_table[s_1][s_2], end=" ")

    print()
print()
for s_1 in range(1, num_s + 1):
    for s_2 in range(1, num_s + 1):
        for k in range(1, num_s + 1):
            comparison_table[s_1][s_2] = min(comparison_table[s_1][s_2],
                                             comparison_table[s_1][k] + comparison_table[k][s_2])
answer = []
a_pass = 0
for s_1 in range(1, num_s + 1):
    a_pass = 0
    for s_2 in range(1, num_s + 1):

        if comparison_table[s_1][s_2] == INF:
            if comparison_table[s_2][s_1] == INF:
                a_pass += 1
                break
    if a_pass == 0:
        answer.append(s_1)

print(answer)

