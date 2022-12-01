def search_bfs(x, y):

    que = deque()
    que.append((x, y))

    while que:
        now_x, now_y = que.popleft()

        for way in way_4:
            next_x = now_x + way[0]
            next_y = now_y + way[1]

            if 0 <= next_x < in_n and 0 <= next_y < in_m:
                if in_g[next_x][next_y] == 1:
                    in_g[next_x][next_y] = in_g[now_x][now_y] + 1
                    que.append((next_x, next_y))

    return in_g[in_n - 1][in_m - 1]


if __name__ == "__main__":

    from collections import deque
    import sys

    in_n, in_m = map(int, sys.stdin.readline().split())

    in_g = list()
    for _ in range(in_n):
        in_g.append(list(map(int, sys.stdin.readline().rstrip())))

    way_4 = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    print(search_bfs(0, 0,))
