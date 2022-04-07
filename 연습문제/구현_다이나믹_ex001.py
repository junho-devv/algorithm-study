def solution(a_row, a_col, a_list):
    answer = 0
    temp_list = [[0] * a_col for _ in range(a_row)]
    for r in range(a_row):
        for c in range(a_col):
            temp_list[r][c] = a_list[c + r * a_col]

    for c in range(1, a_col):
        for r in range(0, a_row):
            max_val = 0
            for x in [-1, 0, 1]:
                if 0 <= r + x < a_row:
                    max_val = max(max_val, temp_list[r + x][c - 1])
            temp_list[r][c] += max_val

    for x in range(a_row):
        answer = max(answer, temp_list[x][a_col - 1])
    print(temp_list)
    return answer


# 테스트 케이스의 개수(t_num) 입력하기
t_num = int(input())
list_a = []
# 테스트 케이스 입력하기
for _ in range(t_num):
    row_a, col_a = map(int, input().split())
    list_a.append((row_a, col_a, list(map(int, input().split()))))

for i in list_a:
    print(solution(i[0], i[1], i[2]))
