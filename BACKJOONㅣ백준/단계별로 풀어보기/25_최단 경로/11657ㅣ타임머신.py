import sys


INF = sys.maxsize


in_n, in_m = map(int, sys.stdin.readline().split())
edge_m = []
for _ in range(in_m):
    in_a, in_b, in_c = map(int, sys.stdin.readline().split())
    edge_m.append((in_a, in_b, in_c))

distance_n = [INF] * (in_n + 1)


def bellman_ford(para_start):
    distance_n[para_start] = 0
    for cnt_repeat in range(1, in_n + 1):
        for edge in edge_m:
            temp_node = edge[0]
            next_node = edge[1]
            temp_cost = edge[2]

            if distance_n[temp_node] != INF and distance_n[next_node] > distance_n[temp_node] + temp_cost:
                distance_n[next_node] = distance_n[temp_node] + temp_cost
                if cnt_repeat == in_n:
                    return True
    return False


if bellman_ford(1):
    print(-1)
else:
    for n in range(2, in_n + 1):
        print(distance_n[n] if distance_n[n] != INF else -1)
