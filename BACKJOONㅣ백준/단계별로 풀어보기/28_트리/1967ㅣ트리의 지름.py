from collections import deque
import sys


def search(para_start):
    answer = [0, 0]

    visit = [-1 for _ in range(in_n + 1)]
    visit[para_start] = 0

    que_node = deque([para_start])
    while que_node:
        temp_node = que_node.popleft()
        for node, cost in tree_n[temp_node]:
            if visit[node] == -1:
                visit[node] = visit[temp_node] + cost
                que_node.append(node)

                if answer[1] < visit[node]:
                    answer = [node, visit[node]]

    return answer


if __name__ == '__main__':
    in_n = int(sys.stdin.readline())

    tree_n = [[] for _ in range(in_n + 1)]
    for _ in range(in_n - 1):
        in_a, in_b, in_c = map(int, sys.stdin.readline().split())
        tree_n[in_a].append([in_b, in_c])
        tree_n[in_b].append([in_a, in_c])

    out_node, out_diameter = search(1)
    out_node, out_diameter = search(out_node)

    print(out_diameter)
