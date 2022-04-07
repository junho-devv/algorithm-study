from itertools import permutations


def solution():
    # end_x, num_x = map(int, input().split())
    #
    # list_x = [x for x in range(1, end_x + 1)]
    #
    # list_y = list(permutations(list_x, num_x))
    #
    # for y in list_y:
    #     for i in y:
    #         print(i, end=' ')
    #     print()

    input_n, input_m = map(int, input().split())


def solution_2():
    input_n, input_m = map(int, input().split())
    list_visited = [False] * input_n
    out = []

    def solve(para_depth, para_n, para_m):

        if para_depth == para_m:
            print(' '.join(map(str, out)))
            return

        for i in range(input_n):

            if not list_visited[i]:
                list_visited[i] = True
                out.append(i + 1)
                solve(para_depth + 1, input_n, input_m)
                list_visited[i] = False
                out.pop()

    solve(0, input_n, input_m)


solution_2()
