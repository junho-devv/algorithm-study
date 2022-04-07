def solution(citations):
    answer = 0

    citations.sort()
    print(citations)
    c_l, c_r = 0, len(citations)

    while c_l <=c_r:
        print(c_l, c_r)
        c_m = (c_l + c_r) // 2
        print(c_m, citations[c_m])
        if c_m + 1 <= citations[c_m] <= len(citations) - c_m:
            c_l = c_m + 1
        else:
            c_r = c_m - 1

    print(c_m)
    return answer


if __name__ == '__main__':
    in_x = [3, 0, 6, 1, 5]

    solution(in_x)
