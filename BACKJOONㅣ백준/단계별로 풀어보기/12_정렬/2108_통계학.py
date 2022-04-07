from collections import Counter


def solution():
    # 입력할 수의 개수(num_n) 입력받기
    num_n = int(input())
    # 입력한 수를 저장할 배열(arr_n)
    arr_n = []
    # 수 입력받기
    for _ in range(num_n):
        arr_n.append(int(input()))
    # 배열 안의 수를 오름차순으로 정렬하기
    arr_n.sort()

    # 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
    answer_1 = round(sum(arr_n) / num_n)
    print(answer_1)

    # 중앙값을 출력한다.
    mid_n = num_n // 2
    answer_2 = arr_n[mid_n]
    print(answer_2)

    # 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
    count_arr_n = Counter(arr_n).most_common()

    if len(count_arr_n) > 1 and count_arr_n[0][1] == count_arr_n[1][1]:
        answer_3 = count_arr_n[1][0]
    else:
        answer_3 = count_arr_n[0][0]
    print(answer_3)

    # 범위를 출력한다.
    answer_4 = max(arr_n) - min(arr_n)
    print(answer_4)

    return


solution()
