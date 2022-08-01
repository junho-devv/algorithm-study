# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a_list):

    # 행의 개수, 세로수
    row_len = len(a_list)
    # 열의 개수, 가로수
    col_len = len(a_list[0])

    a_result = [[0] * row_len for _ in range(col_len)]

    for x in range(row_len):
        for y in range(col_len):
            a_result[y][row_len - x - 1] = a_list[x][y]

    return a_result


# 2차원 리스트 180도 회전
def rotate_a_matrix_by_180_degree(a_list):

    # 행의 개수, 세로수
    row_len = len(a_list)
    # 열의 개수, 가로수
    col_len = len(a_list[0])

    a_result = [[0] * col_len for _ in range(row_len)]

    for x in range(row_len):
        for y in range(col_len):
            a_result[row_len - x - 1][col_len - y - 1] = a_list[x][y]

    return a_result


def check_1(new_lock):
    lock_length = len(new_lock) // 3

    for x in range(lock_length, lock_length * 2):
        for y in range(lock_length, lock_length * 2):

            if new_lock[x][y] != 1:
                return False

    return True


def solution(key, lock):

    answer = False

    lock_len = len(lock)
    key_len = len(key)

    new_lock = [[0] * (lock_len * 3) for _ in range(lock_len * 3)]

    for x in range(lock_len):
        for y in range(lock_len):
            new_lock[x + lock_len][y + lock_len] = lock[x][y]

    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)

        for x in range(1, lock_len * 2):
            for y in range(1, lock_len * 2):

                for a in range(key_len):
                    for b in range(key_len):
                        new_lock[x + a][y + b] += key[a][b]

                if check_1(new_lock):
                    answer = True

                for a in range(key_len):
                    for b in range(key_len):
                        new_lock[x + a][y + b] -= key[a][b]

    return answer


a_key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
a_lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(a_key, a_lock))
