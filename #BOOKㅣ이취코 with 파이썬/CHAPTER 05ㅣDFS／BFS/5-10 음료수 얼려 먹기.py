def dfs(x, y):

    if x <= -1 or x >= in_n or y <= -1 or y >= in_m:
        return False

    if in_g[x][y] == 0:
        in_g[x][y] = 1

        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)

        return True

    return False


if __name__ == "__main__":

    import sys

    in_n, in_m = map(int, sys.stdin.readline().split())

    in_g = list()
    for _ in range(in_n):
        in_g.append(list(map(int, sys.stdin.readline())))

    out_1 = 0
    for n in range(in_n):
        for m in range(in_m):
            if dfs(n, m):
                out_1 += 1

    print(out_1)
