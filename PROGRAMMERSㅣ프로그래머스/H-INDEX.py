def solution(citations):
    answer = 0

    citations.sort()

    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            answer = len(citations) - idx
            return answer

    return answer

    citation.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx

    return len(citations)


if __name__ == '__main__':
    in_x = [3, 0, 6, 1, 5]

    solution(in_x)
