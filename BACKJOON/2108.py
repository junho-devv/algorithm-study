from collections import Counter

num_n = int(input())
seq_x = []

for _ in range(num_n):
    seq_x.append(int(input()))
seq_x.sort()


def solution():

    # 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
    answer_1 = round(sum(seq_x) / num_n)
    print(answer_1)

    # 중앙값을 출력한다.
    mid = (num_n - 1) // 2
    answer_2 = seq_x[mid]
    print(answer_2)

    # 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
    count_seq_x = Counter(seq_x).most_common()

    if len(count_seq_x) > 1 and count_seq_x[0][1] == count_seq_x[1][1]:
        answer_3 = count_seq_x[1][0]
    else:
        answer_3 = count_seq_x[0][0]
    print(answer_3)

    # 범위를 출력한다.
    answer_4 = max(seq_x) - min(seq_x)
    print(answer_4)

    return


def simple_function():
    seq_a = [-1, 0, 1, 2, 3, 7, 10]
    len_a = len(seq_a)
    temp = list(set(seq_a))
    temp.sort()
    seq_max = []
    cnt_max = 0

    for i in temp:
        if cnt_max == seq_a.count(i):
            seq_max.append(i)

        elif cnt_max < seq_a.count(i):
            seq_max = [i]
            cnt_max = seq_a.count(i)

    print(seq_max)


# solution()
simple_function()
