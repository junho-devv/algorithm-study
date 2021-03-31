def find_parent_node(parent_node_list, c_node):

    if parent_node_list[c_node] != c_node:
        parent_node_list[c_node] = find_parent_node(parent_node_list, parent_node_list[c_node])

    return parent_node_list[c_node]


def union(parent_node_list, a_node, b_node):

    a_node = find_parent_node(parent_node_list, a_node)
    b_node = find_parent_node(parent_node_list, b_node)

    if a_node < b_node:
        parent_node_list[b_node] = a_node
    else:
        parent_node_list[a_node] = b_node


n_num, e_num = map(int, input().split())

parents = [0] * (n_num + 1)
edges = []

for i in range(1, n_num + 1):
    parents[i] = i

for _ in range(e_num):
    a_node, b_node, ab_cost = map(int, input().split())
    edges.append([ab_cost, a_node, b_node])

edges.sort()

mst_result = 0

for edge in edges:

    ab_cost, a_node, b_node = edge

    if find_parent_node(parents, a_node) != find_parent_node(parents, b_node):
        union(parents, a_node, b_node)
        mst_result += ab_cost

print(mst_result)
print(parents)
