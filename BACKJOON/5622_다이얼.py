def solution():
    answer = 0
    input_x = input()
    for i in input_x:
        if i == "Z":
            answer += 9 + 1
        else:
            answer += ((ord(i) - 65) // 3 + 2) + 1

    print(answer)

    return


solution()
