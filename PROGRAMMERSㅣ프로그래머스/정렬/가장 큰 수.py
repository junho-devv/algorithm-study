import sys


def solution(numbers):
    answer = ''

    numbers.sort()
    numbers = list(map(str, numbers))

    max_len = len(numbers[-1])

    numbers.sort(reverse=True, key=lambda x: x * max_len)

    result_str = ''.join(numbers)
    if int(result_str):
        answer = result_str
    else:
        answer = '0'

    return answer


if __name__ == '__main__':
    # in_x = list(map(int, sys.stdin.readline().split()))
    in_x = [3, 30, 34, 5, 9]
    solution(in_x)
