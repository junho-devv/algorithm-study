import sys
from collections import deque


in_n = int(sys.stdin.readline())
in_m = int(sys.stdin.readline())
graph_nm = [[False for _ in range(in_n + 1)] for _ in range(in_n + 1)]
for _ in range(in_m):
    start_m, end_m = map(int, sys.stdin.readline().split())
    graph_nm[start_m][end_m] = graph_nm[end_m][start_m] = True

visited_nm = [False] * (in_n + 1)


def infect_computers(para_node, para_answer):
    visited_nm[para_node] = True

    que_node = deque([para_node])

    while que_node:
        infected_node = que_node.popleft()

        for node in range(1, in_n + 1):
            if not visited_nm[node] and graph_nm[infected_node][node]:
                visited_nm[node] = True
                que_node.append(node)

                para_answer += 1

    return para_answer


print(infect_computers(1, 0))
