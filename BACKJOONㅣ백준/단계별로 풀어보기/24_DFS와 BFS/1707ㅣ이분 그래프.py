from collections import deque
import sys


def determine(para_v):
    color_v[para_v] = 1

    que_v = deque([v])
    while que_v:
        temp_v = que_v.popleft()
        for next_v in graph_v[temp_v]:
            if color_v[next_v] == 0:
                color_v[next_v] = -color_v[temp_v]
                que_v.append(next_v)
            else:
                if color_v[next_v] == color_v[temp_v]:
                    return False
    return True


in_k = int(sys.stdin.readline())
for _ in range(in_k):
    in_v, in_e = map(int, sys.stdin.readline().split())

    graph_v = [[] for _ in range(in_v + 1)]
    color_v = [0] * (in_v + 1)
    for _ in range(in_e):
        point_a, point_b = map(int, sys.stdin.readline().split())
        graph_v[point_a].append(point_b)
        graph_v[point_b].append(point_a)

    for v in range(1, in_v + 1):
        if color_v[v] == 0 and not determine(v):
            print("NO")
            break
    else:
        print("YES")

# 참조 : https://gmlwjd9405.github.io/2018/08/23/algorithm-bipartite-graph.html
