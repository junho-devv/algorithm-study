import sys


def calculate(para_a, para_b):
    return abs(para_a[0] - para_b[0]) + abs(para_a[1] - para_b[1])


def search(para_cop_1, para_cop_2):
    if dp_dist[para_cop_1][para_cop_2] != -1:
        return dp_dist[para_cop_1][para_cop_2]

    next_task = max(para_cop_1, para_cop_2) + 1
    if next_task == in_w + 2:
        return 0

    solver_1 = search(next_task, para_cop_2) + calculate(list_task[para_cop_1], list_task[next_task])
    solver_2 = search(para_cop_1, next_task) + calculate(list_task[para_cop_2], list_task[next_task])

    if solver_1 < solver_2:
        dp_dist[para_cop_1][para_cop_2] = solver_1
        dp_solver[para_cop_1][para_cop_2] = 1
    else:
        dp_dist[para_cop_1][para_cop_2] = solver_2
        dp_solver[para_cop_1][para_cop_2] = 2

    return dp_dist[para_cop_1][para_cop_2]


if __name__ == '__main__':
    MAX = int(1e3) + 5

    in_n = int(sys.stdin.readline())
    in_w = int(sys.stdin.readline())

    list_task = [(1, 1), (in_n, in_n)]
    for _ in range(in_w):
        list_task.append(tuple(map(int, sys.stdin.readline().split())))

    dp_dist = [[-1 for _ in range(MAX)] for _ in range(MAX)]
    dp_solver = [[0 for _ in range(MAX)] for _ in range(MAX)]

    pos_cop_1, pos_cop_2 = 0, 1

    answer_1 = search(pos_cop_1, pos_cop_2)
    print(answer_1)

    while max(pos_cop_1, pos_cop_2) + 1 < in_w + 2:
        answer_2 = dp_solver[pos_cop_1][pos_cop_2]
        print(answer_2)

        if dp_solver[pos_cop_1][pos_cop_2] == 1:
            pos_cop_1 = max(pos_cop_1, pos_cop_2) + 1
        else:
            pos_cop_2 = max(pos_cop_1, pos_cop_2) + 1
