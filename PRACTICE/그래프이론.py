def find_parent_node(parent, x):

    if parent[x] != x:
        return find_parent_node(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent_node(parent, a)
    b = find_parent_node(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n_num, e_num = map(int, input().split())
parent = [0] * (n_num + 1)

for i in range(1, n_num + 1):
    parent[i] = i

for e in range(e_num):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합: ", end='')
for i in range(1, n_num + 1):
    print(find_parent_node(parent, i), end=' ')

print()

print("부모 테이블: ", end='')
for i in range(1, n_num + 1):
    print(parent[i], end=' ')
