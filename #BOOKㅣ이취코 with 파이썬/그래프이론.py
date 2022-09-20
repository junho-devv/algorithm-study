def find_parent_node(p_node_list, c_node):

    if p_node_list[c_node] != c_node:
        return find_parent_node(p_node_list, p_node_list[c_node])

    return c_node


def union_parent(p_node_list, a_node, b_node):

    a_node = find_parent_node(p_node_list, a_node)
    b_node = find_parent_node(p_node_list, b_node)

    if a_node < b_node:
        p_node_list[b_node] = a_node
    else:
        p_node_list[a_node] = b_node


if __name__ == "__main__":

    import sys

    n_num, e_num = map(int, sys.stdin.readline().split())
    parent = [0] * (n_num + 1)

    for i in range(1, n_num + 1):
        parent[i] = i

    for e in range(e_num):
        a, b = map(int, sys.stdin.readline().split())
        union_parent(parent, a, b)

    print("각 원소가 속한 집합: ", end='')
    for i in range(1, n_num + 1):
        print(find_parent_node(parent, i), end=' ')

    print()

    print("부모 테이블: ", end='')
    for i in range(1, n_num + 1):
        print(parent[i], end=' ')
