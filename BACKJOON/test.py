import sys


def solution(array, commands):
    answer = []

    for command in commands:
        sub_array = array[command[0] - 1:command[1]]
        sub_array.sort()
        answer.append(sub_array[command[2] - 1])

    return answer


if __name__ == '__main__':

    in_a, in_b = [1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    print(in_a[0:1])
    print(solution(in_a, in_b))