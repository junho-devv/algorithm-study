def solution(numbers):
    answer = 0

    from itertools import permutations

    temp_set = set()
    for _ in range(len(numbers)):
        temp_set |= set(map(int, map(''.join, permutations(numbers, _ + 1))))

    temp_set -= set([0, 1])

    for _ in range(2, int(max(temp_set) ** 0.5) + 1):
        temp_set -= set(range(_ * 2, max(temp_set) + 1, _))

    answer += len(temp_set)

    return answer


if __name__ == '__main__':
    in_n = "011"

    solution(in_n)
