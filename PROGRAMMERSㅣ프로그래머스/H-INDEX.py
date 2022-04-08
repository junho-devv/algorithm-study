# 오름차순으로 해결하기
def solution(citations):
    answer = 0

    citations.sort()

    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            answer = len(citations) - idx
            return answer

    return answer


# 내림차순으로 해결하기
def descending_sort(citations):
    citations.sort(reverse=True)
    print(citations)
    for idx, citation in enumerate(citations):
        print(idx, citation)
        if idx >= citation:
            return idx

    return len(citations)


if __name__ == '__main__':
    in_x = [6, 8, 7, 11, 15]

    solution(in_x)
    descending_sort(in_x)


# https://en.wikipedia.org/wiki/H-index

# H-INDEX(H-지수)란?
# H-지수는 특정 연구원의 연구성과를 평가하기 위한 지표로써, 발표한 논문수와 피인용수를 이용하여 객관적으로 학문적 역량을 측정할 수 있습니다.
