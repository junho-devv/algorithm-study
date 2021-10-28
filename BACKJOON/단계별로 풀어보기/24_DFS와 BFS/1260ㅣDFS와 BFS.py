import sys
from collections import deque


in_n, in_m, in_v = map(int, sys.stdin.readline().split())
graph_nm = [[False for _ in range(in_n + 1)] for _ in range(in_n + 1)]
for _ in range(in_m):
    start_m, end_m = map(int, sys.stdin.readline().split())
    graph_nm[start_m][end_m] = graph_nm[end_m][start_m] = True

visited_dfs, answer_dfs = [False] * (in_n + 1), []
visited_bfs, answer_bfs = [False] * (in_n + 1), []


def dfs(para_node):
    visited_dfs[para_node] = True
    answer_dfs.append(para_node)
    for node in range(1, in_n + 1):
        if not visited_dfs[node] and graph_nm[para_node][node]:
            dfs(node)


def bfs(para_node):
    que_bfs = deque([para_node])

    visited_bfs[para_node] = True
    answer_bfs.append(para_node)

    while que_bfs:
        current_node = que_bfs.popleft()
        for next_node in range(1, in_n + 1):
            if not visited_bfs[next_node] and graph_nm[current_node][next_node]:
                que_bfs.append(next_node)
                visited_bfs[next_node] = True
                answer_bfs.append(next_node)


dfs(in_v)
print(*answer_dfs)

bfs(in_v)
print(*answer_bfs)
