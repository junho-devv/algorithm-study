def solution():
    # 크로아티아 알파벳의 개수(answer)
    answer = 0
    # 크로아티아 알파벳 목록
    arr_x = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    # 문자열 X(input_x) 입력받기
    input_x = input()
    # 문자열 X가 몇 개의 크로아티아 알파벳으로 이뤄져있는지 계산하기
    for i in arr_x:
        count_x = input_x.count(i)
        # 해당 알파벳이 문자열 X내에 존재한다면,
        if count_x != 0:
            input_x = input_x.replace(i, "0")
            answer += count_x
    # 목록에 있는 알파벳을 제외한 나머지의 개수
    answer += len(input_x.replace("0", ""))
    # 결과 출력하기
    print(answer)


def solution_2():
    # 크로아티아 알파벳의 개수(answer)
    answer = 0
    # 크로아티아 알파벳 목록
    arr_x = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=']
    # 문자열 X(input_x) 입력받기
    input_x = input()
    # 문자열 X의 길이(len_x)
    len_x = len(input_x)
    # 문자열 X가 몇 개의 크로아티아 알파벳으로 이뤄져있는지 계산하기
    for i in arr_x:
        count_x = input_x.count(i)
        # 해당 알파벳이 문자열 X내에 존재한다면,
        if count_x != 0:
            answer += count_x
            len_x -= len(i) * count_x
    print(answer, len_x)
    count_y1 = input_x.count('dz=')
    count_y2 = input_x.count('z=')

    print(count_y2 - count_y1)
    answer += count_y2 - count_y1
    len_x -= len('z=') * (count_y2 - count_y1)
    print(answer, len_x)
    # 목록에 있는 알파벳을 제외한 나머지의 개수
    answer += len_x
    # 결과 출력하기
    print(answer)


solution()
