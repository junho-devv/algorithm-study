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
    seq_temp = [0] * (max(seq_x) + 1)

    for i in range(num_n):
        seq_temp[seq_x[i]] += 1
    seq_max = []
    for i in range(len(seq_temp)):
        if seq_temp[i] == max(seq_temp):
            seq_max.append(i)
    if len(seq_max) == 1:
        answer_3 = seq_max[0]
    else:
        answer_3 = seq_max[1]
    print(seq_max)
    print(answer_3)

    # 범위를 출력한다.
    answer_4 = max(seq_x) - min(seq_x)
    print(answer_4)

    return


solution()

