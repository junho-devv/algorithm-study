from math import sqrt


while True:

    input_x = int(input())

    if input_x == 0:
        break
    # 소수의 개수(num_pn)
    num_pn = 0
    # input_x 보다 크고 2 * input_x 보다 작거나 같은 소수의 개수(num_pn) 구하기
    for i in range(input_x + 1, 2 * input_x + 1):

        for j in range(2, int(sqrt(i) + 1)):
            if i % j == 0:
                break
        else:
            num_pn += 1

    print(num_pn)
