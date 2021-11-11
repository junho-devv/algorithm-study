import sys


def find(para_n):
    answer = [2]
    for n in range(3, para_n + 1):
        for m in range(2, int(n ** 0.5) + 1):
            if n % m == 0:
                break
        else:
            answer.append(n)

    return answer


def count(para_list, para_len):
    answer = 0

    start, end = 0, 0
    temp_sum = para_list[0]
    while start < para_len:
        if temp_sum == in_n:
            answer += 1

        if temp_sum >= in_n or end == para_len - 1:
            temp_sum -= para_list[start]
            start += 1
        else:
            end += 1
            temp_sum += para_list[end]

    return answer


if __name__ == '__main__':
    in_n = int(sys.stdin.readline())

    list_pn = find(in_n)

    print(count(list_pn, len(list_pn)))
