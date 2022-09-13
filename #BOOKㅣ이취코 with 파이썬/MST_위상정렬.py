from collections import deque


def topology_sort():

    a_result = []
    a_que = deque()

    for i in range(1, n_num + 1):
        if in_degree[i] == 0:
            a_que.append(i)

    while a_que:

        now = a_que.popleft()
        a_result.append(now)

        for i in graph[now]:
            in_degree[i] -= 1

            if in_degree[i] == 0:
                a_que.append(i)

    for i in a_result:
        print(i, end=' ')


# 노드의 개수(num_n), 간선의 개수(num_e) 입력하기
n_num, e_num = map(int, input().split())
# in-degree(진입차수)
in_degree = [0] * (n_num + 1)
graph = [[] for _ in range(n_num + 1)]

for _ in range(e_num):
    a_node, b_node = map(int, input().split())
    graph[a_node].append(b_node)
    in_degree[b_node] += 1

topology_sort()
