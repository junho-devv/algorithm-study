def solution(n, results):

    graph_w = [set() for _ in range(n + 1)]
    graph_l = [set() for _ in range(n + 1)]

    for winner, loser in results:
        graph_w[loser].add(winner)
        graph_l[winner].add(loser)

    for player in range(1, n + 1):
        for winner in graph_w[player]:
            graph_l[winner].update(graph_l[player])
        for loser in graph_l[player]:
            graph_w[loser].update(graph_w[player])

    answer = 0

    for player in range(1, n + 1):
        if len(graph_w[player]) + len(graph_l[player]) == n - 1:
            answer += 1

    return answer


if __name__ == '__main__':
    in_n = 5
    in_r = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

    print(solution(in_n, in_r))
