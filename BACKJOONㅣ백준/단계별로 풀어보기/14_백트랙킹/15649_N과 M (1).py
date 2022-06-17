def solve(depth, n, m, visited, out):

    if depth == m:
        print(' '.join(map(str, out)))
        return

    for idx in range(n):

        if not visited[idx]:
            visited[idx] = True
            out.append(idx + 1)

            solve(depth + 1, n, m, visited, out)

            visited[idx] = False
            out.pop()


# DFS/백트랙킹 이용한 풀이법
def solution(n, m):

    visited = [False] * n
    answer = []

    solve(0, n, m, visited, answer)


if __name__ == "__main__":

    import sys

    in_n, in_m = map(int, sys.stdin.readline().split())

    solution(in_n, in_m)
