def solution(a_list):

    cave = [[0] * a_col for _ in range(a_row)]
    for i in range(0, a_col, 2):
        for j in range(a_list[i]):
            cave[j][i] = 1

    for i in range(1, a_col, 2):
        for j in range(a_list[i]):
            cave[a_row - j - 1][i] = 1

    answer = [0] * a_row
    for i in range(a_row):
        answer[i] = sum(cave[i])

    a_result = min(answer)
    b_result = answer.count(a_result)

    answer = str(a_result) + " " + str(b_result)

    return answer


a_col, a_row = map(int, input().split())
c_list = []
for _ in range(a_col):
    c_list.append(int(input()))

print(solution(c_list))
