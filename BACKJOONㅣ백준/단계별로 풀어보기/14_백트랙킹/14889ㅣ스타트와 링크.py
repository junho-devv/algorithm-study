def solution(n, stats):

    def depth_first_search(depth, index):

        nonlocal minimum_gap

        if depth == n // 2:
            team_s, team_l = 0, 0
            for idx_1 in range(n):
                for idx_2 in range(n):
                    if visit[idx_1] and visit[idx_2]:
                        team_s += stats[idx_1][idx_2]
                    elif not visit[idx_1] and not visit[idx_2]:
                        team_l += stats[idx_1][idx_2]

            minimum_gap = min(minimum_gap, abs(team_s - team_l))
            return

        for idx in range(index, n):
            if not visit[idx]:
                visit[idx] = True
                depth_first_search(depth + 1, index + 1)
                visit[idx] = False

    visit = [False for _ in range(n)]
    minimum_gap = int(1e9)

    depth_first_search(0, 0)

    answer = minimum_gap
    return answer


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())
    in_s = [list(map(int, sys.stdin.readline().split())) for _ in range(in_n)]

    print(solution(in_n, in_s))
