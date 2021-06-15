# LCS(Longest Common Subsequence, 최장 공통 부분수열)

str_a = input()
str_b = input()

len_a = len(str_a)
len_b = len(str_b)


def solution():

    graph_x = [[0] * (len_a + 1) for _ in range(len_b + 1)]

    for a in range(1, len_a + 1):
        for b in range(1, len_b + 1):

            if str_a[a - 1] == str_b[b - 1]:
                if graph_x[b][a - 1] > graph_x[b - 1][a]:
                    graph_x[b][a] = graph_x[b][a - 1]
                else:
                    graph_x[b][a] = graph_x[b - 1][a] + 1

            else:
                if graph_x[b][a - 1] > graph_x[b - 1][a]:
                    graph_x[b][a] = graph_x[b][a - 1]
                else:
                    graph_x[b][a] = graph_x[b - 1][a]

    for i in range(len_b + 1):
        print(graph_x[i])
        print()
    # answer = LCS
    answer = graph_x[len_b][len_a]

    return answer


print(solution())