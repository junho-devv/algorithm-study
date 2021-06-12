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
                graph_x[b][a] = graph_x[b][a - 1] + 1
            else:
                graph_x[b][a] = graph_x[b][a - 1]

    print(graph_x)
    answer = 0
    return answer


print(solution())
