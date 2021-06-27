# 문자열 제곱
def calculate_failure(a_str):
    answer = [0] * len(a_str)
    # 인덱스(idx)는 반복되는 문자열의 마지막 지점을 가리킨다
    idx = 0
    # 실패함수(Failure Function) 구현
    for i in range(1, len(a_str)):
        # 패턴이 일치하지 않을 때
        while idx > 0 and a_str[i] != a_str[idx]:
            # idx = 0
            idx = answer[idx - 1]
        # 패턴이 일치할 때
        if a_str[i] == a_str[idx]:
            idx += 1
            answer[i] = idx

    return answer


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
            # 문자열(str_s)의 실패함수를 (table)에 초기화
            table = calculate_failure(str_s)

            if len_s % (len_s - table[-1]) != 0:
                answer = 1
            else:
                answer = len_s // (len_s - table[-1])
        print(answer)

    return


solution()
