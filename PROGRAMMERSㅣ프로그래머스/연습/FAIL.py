def solution(num, stages):
    answer = []

    temp_list = [0] * (max(stages) + 1)
    for s in stages:
        temp_list[s] += 1

    a_result = []
    c_num = len(stages)

    for i in range(1, num + 1):
        a_failure = temp_list[i] / c_num
        c_num -= temp_list[i]
        a_result.append((a_failure, i))

    a_result.sort(reverse=True, key=lambda x: x[0])

    for a in a_result:
        answer.append(a[1])

    return answer


if __name__ == "__main__":

    import sys

    s_num = int(sys.stdin.readline())
    s_list = list(map(int, input().split()))

    print(solution(s_num, s_list))
