import sys


s_num, f_num = map(int, sys.stdin.readline().split())

team_graph = [0] * (s_num + 1)

for i in range(s_num + 1):
    team_graph[i] = i


def check_a_team(graph, x_student):

    if graph[x_student] != x_student:
        graph[x_student] = check_a_team(graph, graph[x_student])

    return x_student


def form_a_team(graph, x_student, y_student):

    x_student = check_a_team(graph, x_student)
    y_student = check_a_team(graph, y_student)

    if x_student < y_student:
        graph[y_student] = x_student
    else:
        graph[x_student] = y_student


for _ in range(f_num):

    m, a_student, b_student = map(int, input().split())

    if m == 0:
        form_a_team(team_graph, a_student, b_student)

    if m == 1:
        a_student = check_a_team(team_graph, a_student)
        b_student = check_a_team(team_graph, b_student)

        if a_student != b_student:
            print("NO")
        else:
            print("YES")
