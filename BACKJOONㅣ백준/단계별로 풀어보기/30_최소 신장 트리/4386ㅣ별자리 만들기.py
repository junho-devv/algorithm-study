import sys


def calculate(para_x1, para_y1, para_x2, para_y2):
    answer = (para_x1 - para_x2) ** 2 + (para_y1 - para_y2) ** 2
    return round(answer ** 0.5, 2)


def find(para_node):
    if parent_node[para_node] != para_node:
        parent_node[para_node] = find(parent_node[para_node])

    return parent_node[para_node]


def union(para_node1, para_node2):
    root_n1, root_n2 = find(para_node1), find(para_node2)
    if root_n1 > root_n2:
        root_n1, root_n2 = root_n2, root_n1

    parent_node[root_n2] = root_n1


if __name__ == '__main__':
    in_n = int(sys.stdin.readline())

    star_n = []
    for _ in range(in_n):
        in_x, in_y = map(float, sys.stdin.readline().split())
        star_n.append((in_x, in_y))

    dist_n = []
    for star_1 in range(in_n):
        for star_2 in range(star_1 + 1, in_n):
            distance = calculate(star_n[star_1][0], star_n[star_1][1], star_n[star_2][0], star_n[star_2][1])
            dist_n.append([distance, star_1, star_2])
    dist_n.sort(key=lambda d: d[0])

    parent_node = [_ for _ in range(in_n)]
    out_min = 0
    for cost, n1, n2 in dist_n:
        if find(n1) != find(n2):
            union(n1, n2)
            out_min += cost

    print(out_min)
