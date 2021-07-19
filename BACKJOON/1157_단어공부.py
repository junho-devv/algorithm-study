def solution():

    input_x = input()

    arr_x = [0] * 26

    for i in input_x:
        # 알파벳이 대문자라면, ( 65 ~ 90 )
        if ord(i) <= 90:
            arr_x[ord(i) - 65] += 1
        # 알파벳이 소문자라면, ( 97 ~ 122 )
        elif ord(i) >= 97:
            arr_x[ord(i) - 97] += 1
    # 가장 많이 사용된 단어의 수(freq_x)
    freq_x = max(arr_x)

    if arr_x.count(freq_x) == 1:
        answer = chr(arr_x.index(freq_x) + 65)
    else:
        answer = "?"

    print(answer)

    return


solution()
