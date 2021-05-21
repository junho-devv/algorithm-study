def find_parent_node(p_node_list, c_node):
    if p_node_list[c_node] != c_node:
        p_node_list[c_node] = find_parent_node(p_node_list, p_node_list[c_node])

    return p_node_list[c_node]


def union_nodes(p_node_list, a_node, b_node):

    a_node = find_parent_node(a_node)
    b_node = find_parent_node(b_node)

    if a_node < b_node:
        p_node_list[b_node] = a_node
    else:
        p_node_list[a_node] = b_node


n_num, e_num = map(int, input().split())
parents = [0] * (n_num + 1)

is_it_cycled = False

for _ in range(e_num):
    a, b = map(int, input().split())
    # 사이클 판별은 무방향 그래프에서 가능하다
    # 두 노드의 부모노드가 같다면 해당 그래프는 사이클이다.
    # 방향 그래프에서 노드의 방문여부를 표시
    # 이미 방문된 노드가 다시 한번 방문된다면 사이클발생
    if find_parent_node(parents, a) == find_parent_node(parents, b):
        is_it_cycled = True
        break

    else:
        union_nodes(parents, a, b)

if is_it_cycled:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")

