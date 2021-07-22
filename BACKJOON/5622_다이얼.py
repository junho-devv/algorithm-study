def solution():
    answer = 0
    input_x = input()

    arr_dial = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'],
                ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

    for i in input_x:
        for j in arr_dial:
            if i in j:
                answer += arr_dial.index(j) + 3

    print(answer)

    return


solution()
