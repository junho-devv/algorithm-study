def solution():

    num_x = int(input())
    arr_x = input()

    answer = 0

    for i in range(num_x):
        answer += int(arr_x[i])

    print(answer)

    return


solution()
