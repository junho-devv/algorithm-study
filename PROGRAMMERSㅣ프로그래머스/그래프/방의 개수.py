def solution(arrows):

    move_9 = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    now_xy = (0, 0)

    from collections import deque, defaultdict

    que_xy = deque([now_xy])
    for arrow in arrows:
        for _ in range(2):
            next_xy = (now_xy[0] + move_9[arrow][0], now_xy[1] + move_9[arrow][1])
            que_xy.append(next_xy)

            now_xy = next_xy

    visited_node = defaultdict(bool)
    visited_path = defaultdict(bool)

    answer = 0

    now_xy = que_xy.popleft()
    visited_node[now_xy] = True

    while que_xy:
        next_xy = que_xy.popleft()

        if visited_node[next_xy]:
            if not visited_path[(now_xy, next_xy)]:
                answer += 1
        else:
            visited_node[next_xy] = True

        visited_path[(now_xy, next_xy)] = True
        visited_path[(next_xy, now_xy)] = True

        now_xy = next_xy

    return answer


if __name__ == '__main__':
    in_a = [6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]

    print(solution(in_a))
