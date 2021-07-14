# 한수


def solution():
    # 한수의 개수(answer)
    answer = 0
    int_x = int(input())

    for i in range(1, int_x + 1):
        # 해당 정수가 두자리수 이하일 때,
        if 1 <= i < 100:
            answer += 1
        # 해당 정수가 세자리수 이상일 때
        elif i >= 100:
            arr_x = str(i)
            len_x = len(arr_x)

            diff_x = int(arr_x[0]) - int(arr_x[1])
            pass_x = True
            for j in range(1, len_x - 1):
                if diff_x != int(arr_x[j]) - int(arr_x[j + 1]):
                    pass_x = False
                    break
            if pass_x:
                answer += 1
    # 결과 출력하기
    print(answer)


solution()
