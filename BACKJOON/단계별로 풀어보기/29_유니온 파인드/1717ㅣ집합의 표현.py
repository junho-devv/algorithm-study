import sys

sys.setrecursionlimit(10 ** 6)


def find_parent_node(para_node):
    if para_node == set_n[para_node]:
        return para_node
    root_node = find_parent_node(set_n[para_node])
    set_n[para_node] = root_node
    return set_n[para_node]


def union(para_a, para_b):
    root_a, root_b = find_parent_node(para_a), find_parent_node(para_b)
    if root_a > root_b:
        set_n[root_a] = root_b
    else:
        set_n[root_b] = root_a


if __name__ == '__main__':
    in_n, in_m = map(int, sys.stdin.readline().split())

    set_n = [n for n in range(in_n + 1)]
    for _ in range(in_m):
        in_cmd, in_a, in_b = map(int, sys.stdin.readline().split())
        if in_cmd == 0:
            union(in_a, in_b)

        else:
            if find_parent_node(in_a) == find_parent_node(in_b):
                print("YES")
            else:
                print("NO")
