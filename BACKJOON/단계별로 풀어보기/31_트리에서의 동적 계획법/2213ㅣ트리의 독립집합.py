import sys


def search(para_start):
    list_visit[para_start] = True
    # para_start 노드를 포함할 때,
    list_dp[para_start][0] = in_w[para_start]
    # para_start 노드를 포함하지 않을 때,
    list_dp[para_start][1] = 0

    for p_child in tree_n[para_start]:
        if not list_visit[p_child]:
            search(p_child)
            list_dp[para_start][0] += list_dp[p_child][1]
            list_dp[para_start][1] += max(list_dp[p_child][0], list_dp[p_child][1])


def trace(para_now, para_prev):
    list_trace[para_now] = True
    # 이전 노드(para_prev)를 포함할 때,
    if para_prev == 0:
        for p_child in tree_n[para_now]:
            if not list_trace[p_child]:
                trace(p_child, 1)
    # 이전 노드(para_prev)를 포함하지 않을 때,
    else:
        # 현재 노드(para_now)를 포함할 때 값이 크다면,
        if list_dp[para_now][0] > list_dp[para_now][1]:
            out_2.append(para_now)
            for p_child in tree_n[para_now]:
                if not list_trace[p_child]:
                    trace(p_child, 0)
        # 현재 노드(para_now)를 포함하지 않을 때 값이 크다면,
        else:
            for p_child in tree_n[para_now]:
                if not list_trace[p_child]:
                    trace(p_child, 1)


if __name__ == '__main__':
    MAX = int(1e4) + 1

    in_n = int(sys.stdin.readline())
    in_w = [0] + list(map(int, sys.stdin.readline().split()))

    tree_n = [[] for _ in range(in_n + 1)]
    for _ in range(in_n - 1):
        in_a, in_b = map(int, sys.stdin.readline().split())
        tree_n[in_a].append(in_b)
        tree_n[in_b].append(in_a)

    list_visit = [False] * MAX
    list_dp = [[0] * 2 for _ in range(MAX)]
    search(1)
    out_1 = max(list_dp[1][0], list_dp[1][1])
    print(out_1)

    list_trace = [False] * MAX
    out_2 = []
    trace(1, 1)
    out_2.sort()
    print(*out_2)
