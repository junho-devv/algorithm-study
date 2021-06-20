# 문자열 제곱
def calculate(a_str, a_len):

    for i in range(1, a_len):
        temp = a_str[0:i]



def solution():
    answer = 1

    while True:
        # 문자열 s(str_s) 입력받기
        str_s = input()
        # 문자열 s의 길이(len_s)
        len_s = len(str_s)

        if str_s == ".":
            break
        elif str_s == "":
            answer = 0
        else:
            calculate(str_s, len_s)

        print(answer)

    return


solution()
