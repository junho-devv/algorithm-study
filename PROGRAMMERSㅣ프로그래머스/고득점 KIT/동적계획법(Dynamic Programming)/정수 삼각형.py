def solution(triangle):

    dp_triangle = [[triangle[0][0]]]
    for h in range(1, len(triangle)):
        dp_triangle.append([0] * len(triangle[h]))

        for idx, t in enumerate(triangle[h]):
            if idx == 0:
                dp_triangle[h][idx] = t + dp_triangle[h - 1][idx]
            elif idx == len(triangle[h]) - 1:
                dp_triangle[h][idx] = t + dp_triangle[h - 1][-1]
            else:
                dp_triangle[h][idx] = t + max(dp_triangle[h - 1][idx - 1], dp_triangle[h - 1][idx])

    answer = max(dp_triangle[-1])

    return answer


if __name__ == '__main__':
    in_t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

    solution(in_t)

    # solution = lambda t, l=[]: max(l) if not t else solution(t[1:],
    #                                                          [max(x, y) + z for x, y, z in zip([0] + l, l + [0], t[0])])
