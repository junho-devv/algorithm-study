def solution(N, number):
    set_possible = [0]
    # if N == number:
    #     return 1
    for case in range(1, 9):
        set_case = {int(str(N) * case)}
        for pivot in range(1, case // 2 + 1):
            for x in set_possible[pivot]:
                for y in set_possible[case - pivot]:
                    print(set_possible)
                    set_case.add(x + y)
                    set_case.add(x - y)
                    set_case.add(y - x)
                    set_case.add(x * y)
                    if y != 0:
                        set_case.add(x / y)
                    if x != 0:
                        set_case.add(y / x)
        if number in set_case:
            return case
        set_possible.append(set_case)

    return -1


if __name__ == '__main__':
    in_n = 5
    in_num = 5

    print(solution(in_n, in_num))
