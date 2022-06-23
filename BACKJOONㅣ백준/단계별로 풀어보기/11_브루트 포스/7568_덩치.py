def solution():

    for p_1 in range(in_n):
        for p_2 in range(in_n):
            # 자기자신과 비교는 생략
            if p_1 == p_2:
                continue

            if info_people[p_1][0] < info_people[p_2][0] and info_people[p_1][1] < info_people[p_2][1]:
                info_people[p_1][2] += 1
    # 결과 출력하기
    for _1, _2, rank in info_people:
        print(rank, end=' ')


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())

    # 전체 사람의 몸무게와 키를 저장할 배열(arr_p)
    info_people = []

    for _ in range(in_n):

        weight, height = map(int, sys.stdin.readline().split())

        info_people.append([weight, height, 1])

    solution()
