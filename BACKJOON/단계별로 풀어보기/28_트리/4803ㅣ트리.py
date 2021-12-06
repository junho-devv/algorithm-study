from collections import deque
import sys


def search(para_node):
    answer = True
    que_node = deque([para_node])
    while que_node:
        temp_node = que_node.popleft()
        if visit[temp_node]:
            answer = False
        else:
            visit[temp_node] = True
            for i in tree_n[temp_node]:
                if not visit[i]:
                    que_node.append(i)
    return answer


if __name__ == '__main__':
    out_tc = 0
    while True:
        out_tc += 1

        in_n, in_m = map(int, sys.stdin.readline().split())
        if [in_n, in_m] == [0, 0]:
            break

        tree_n = [[] for _ in range(in_n + 1)]
        for _ in range(in_m):
            in_a, in_b = map(int, sys.stdin.readline().split())
            tree_n[in_a].append(in_b)
            tree_n[in_b].append(in_a)

        out_tree = 0

        visit = [0] * (in_n + 1)
        for n in range(1, in_n + 1):
            if visit[n]:
                continue
            if search(n) is True:
                out_tree += 1

        if out_tree == 0:
            print("Case {}: No trees.".format(out_tc))
        elif out_tree == 1:
            print("Case {}: There is one tree.".format(out_tc))
        else:
            print("Case {}: A forest of {} trees.".format(out_tc, out_tree))
