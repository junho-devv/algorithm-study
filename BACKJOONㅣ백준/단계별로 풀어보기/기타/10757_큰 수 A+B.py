def solution():

    input_a, input_b = map(str, input().split())

    if len(input_a) < len(input_b):
        input_a, input_b = input_b, input_a

    int_a = [0] * (len(input_a) + 1)
    int_b = [0] * (len(input_a) + 1)

    for i in range(len(input_a)):
        int_a[i + 1] = int(input_a[i])
    for i in range(len(input_b)):
        int_b[i + len(input_a) - len(input_b) + 1] = int(input_b[i])

    answer = []

    for i in range(len(int_a) - 1, 0, -1):

        sum_ab = int_a[i] + int_b[i]

        if sum_ab >= 10:
            int_a[i - 1] += 1
            sum_ab -= 10
        answer.append(sum_ab)

    if int_a[0] == 1:
        answer.append(1)
    for i in reversed(answer):
        print(i, end='')


solution()
