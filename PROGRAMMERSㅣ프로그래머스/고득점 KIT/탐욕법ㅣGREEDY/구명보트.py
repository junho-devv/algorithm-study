def solution(people, limit):

    people.sort(reverse=True)

    idx_l, idx_r = 0, len(people) - 1
    answer = 0

    while idx_l <= idx_r:
        answer += 1

        if people[idx_l] + people[idx_r] <= limit:
            idx_r -= 1

        idx_l += 1

    return answer


if __name__ == '__main__':
    in_p = [70, 50, 80, 50]
    in_l = 100

    print(solution(in_p, in_l))
