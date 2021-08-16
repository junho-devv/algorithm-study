def solution():
    # 숫자 N(input_n) 입력받기
    input_n = int(input())

    int_n = 666

    count_n = 0

    while count_n != input_n:

        if '666' in str(int_n):
            count_n += 1

        int_n += 1

    answer = int_n - 1

    print(answer)


solution()
