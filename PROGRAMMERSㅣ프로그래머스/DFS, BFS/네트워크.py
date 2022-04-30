def solution(n, computers):
    answer = 0

    visited_n = [-1] * n
    for idx in range(n):
        if visited_n[idx] == -1:
            visited_n[idx] =
        for n_idx in range(idx + 1, n):
            if visited_n[n_idx] == -1 and computers[idx][n_idx] == 1:
                visited_n[n_idx] = idx
    print(visited_n)

    return answer


if __name__ == '__main__':
    in_n = 3
    in_c = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

    solution(in_n, in_c)
