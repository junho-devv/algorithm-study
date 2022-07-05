def solution(array, commands):

    answer = []

    for command in commands:
        arr_s, arr_e, arr_k = command

        temp_array = array[arr_s - 1: command[1]]
        temp_array.sort()
        answer.append(temp_array[arr_k - 1])

    return answer


if __name__ == '__main__':

    in_a = [1, 5, 2, 6, 3, 7, 4]
    in_c = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    print(solution(in_a, in_c))
