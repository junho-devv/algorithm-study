def solution(brown, yellow):
    answer = []

    for h in range(1, int(yellow ** 0.5) + 1):
        if yellow % h == 0:
            w = yellow // h
            if 2 * (h + w) == brown - 4:
                answer.append(w + 2)
                answer.append(h + 2)
    print(answer)
    return answer


if __name__ == '__main__':
    in_b, in_y = 24, 24

    solution(in_b, in_y)
