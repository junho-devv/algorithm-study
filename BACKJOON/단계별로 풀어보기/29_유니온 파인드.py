import sys


def find_parent_node(para_node):
    answer = para_node
    if set_n[para_node] != para_node:
        answer = find_parent_node(set_n[para_node])

    return answer


def find(para_a, para_b):
    root_a, root_b = find_parent_node(para_a), find_parent_node(para_b)
    if root_a == root_b:
        return True
    else:
        return False


if __name__ == '__main__':
    in_n, in_m = map(int, sys.stdin.readline().split())

    set_n = [n for n in range(10 ** 6 + 1)]
    for _ in range(in_m):
        in_cmd, in_a, in_b = map(int, sys.stdin.readline().split())

        if in_cmd == 0:
            if in_a > in_b:
                in_a, in_b = in_b, in_a

            set_n[in_b] = in_a

        else:
            out_same = find(in_a, in_b)
            if out_same:
                print("YES")
            else:
                print("NO")
