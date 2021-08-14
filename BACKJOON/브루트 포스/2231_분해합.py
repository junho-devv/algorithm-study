def solution():
    # 자연수 N(input_n) 입력받기
    input_n = int(input())
    # 자연수 N(input_n)의 생성자(answer)
    answer = 0

    for i in range(1, input_n):

        int_n = i

        # 임의의 수의 자기자신과 각 자리수의 합(sum_n)
        sum_n = i
        # sum_n 구하기
        while True:

            if i // 10 == 0:
                sum_n += i % 10
                break

            sum_n += i % 10

            i = i // 10

        if sum_n == input_n:
            answer = int_n
            break

    print(answer)


solution()
