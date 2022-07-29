def solution():

    way_4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    now_x, now_y, now_d = in_c
    visit[now_x][now_y] = True

    answer = 1
    cnt_t = 0

    while True:

        now_d -= 1
        if now_d == -1:
            now_d = 3

        next_x = now_x + way_4[now_d][0]
        next_y = now_y + way_4[now_d][1]

        if in_map[next_x][next_y] == 0 and not visit[next_x][next_y]:
            visit[next_x][next_y] = True
            now_x, now_y = next_x, next_y
            answer += 1
            cnt_t = 0
            continue
        else:
            cnt_t += 1

        if cnt_t == 4:
            next_x = now_x - way_4[now_d][0]
            next_y = now_y - way_4[now_d][1]

            if in_map[next_x][next_y] == 0:
                now_x, now_y = next_x, next_y
            else:
                break
            cnt_t = 0

    return answer


if __name__ == "__main__":

    import sys

    in_n, in_m = map(int, sys.stdin.readline().split())
    in_c = list(map(int, sys.stdin.readline().split()))
    in_map = [list(map(int, sys.stdin.readline().split())) for _ in range(in_n)]

    visit = [[False] * in_m for _ in range(in_n)]

    print(solution())
