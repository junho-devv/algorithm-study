def solution():

    num_x = int(input())
    arr_x = []

    for _ in range(num_x):
        # 입력할 단어(word_x), 해당 단어의 길이(len_x)
        word_x = input()
        len_x = len(word_x)

        arr_x.append((word_x, len_x))

    arr_y = list(set(arr_x))
    arr_y.sort(key=lambda x: (x[1], x[0]))

    for i in arr_y:
        print(i[0])


solution()
