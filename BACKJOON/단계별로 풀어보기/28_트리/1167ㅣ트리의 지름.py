from collections import deque
import sys


def search(para_start):
    answer = [0, 0]

    visit = [-1 for _ in range(in_v + 1)]
    visit[para_start] = 0

    que_node = deque([para_start])
    while que_node:
        temp_node = que_node.popleft()
        for node, cost in tree_v[temp_node]:
            if visit[node] == -1:
                visit[node] = visit[temp_node] + cost
                que_node.append(node)
                if answer[0] < visit[node]:
                    answer = visit[node], node
    return answer


if __name__ == '__main__':
    in_v = int(sys.stdin.readline())
    tree_v = [[] for _ in range(in_v + 1)]
    for _ in range(in_v):
        in_e = list(map(int, sys.stdin.readline().split()))

        for v in range(1, len(in_e) - 2, 2):
            tree_v[in_e[0]].append([in_e[v], in_e[v + 1]])

    out_answer, out_node = search(1)
    out_answer, out_node = search(out_node)
    print(out_answer)


# 트리의 지름 구하기 (증명)
# https://blog.myungwoo.kr/112