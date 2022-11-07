def factorial_iterative(num):

    answer = 1
    for n in range(1, num + 1):
        answer *= n

    return answer


def factorial_recursive(num):

    if num <= 1:
        return 1
    else:
        return num * factorial_recursive(num - 1)


if __name__ == "__main__":
    
    import sys

    in_n = int(sys.stdin.readline())

    print("반복적으로 구현 : ", factorial_iterative(in_n))
    print("재귀적으로 구현 : ", factorial_recursive(in_n))
