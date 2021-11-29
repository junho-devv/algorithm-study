import sys


def search(para_node):
    for node in tree_n[para_node]:
        if parent_node[node] == 0:
            parent_node[node] = para_node
            search(node)


if __name__ == '__main__':
    in_n = int(sys.stdin.readline())

    tree_n = [[] for _ in range(in_n + 1)]
    parent_node = [0 for _ in range(in_n + 1)]

    for _ in range(in_n - 1):
        in_n1, in_n2 = map(int, sys.stdin.readline().split())
        tree_n[in_n1].append(in_n2)
        tree_n[in_n2].append(in_n1)

    search(1)

    for i in range(2, in_n + 1):
        print(parent_node[i])
