def solution():
    # 단어의 개수(answer)
    answer = 0
    # 문자열(input_x) 입력받기
    input_x = input()

    count_x = False

    for i in input_x:
        if i == " ":
            count_x = False
        else:
            if not count_x:
                answer += 1
                count_x = True

    print(answer)
    return


solution()
