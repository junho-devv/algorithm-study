h_num = int(input())
h_list = list(map(int, input().split()))


def solution():

    d_list = []

    for a_antenna in h_list:
        a_dist = 0
        for a_home in h_list:
            a_dist += abs(a_home - a_antenna)
        d_list.append((a_dist, a_antenna))

    d_list.sort(key=lambda position: position[0])
    print(d_list)

    answer = d_list[0][1]
    print(answer)
    return answer


solution()
