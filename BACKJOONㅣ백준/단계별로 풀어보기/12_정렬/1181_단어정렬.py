def solution():

    arr_x = []

    for _ in range(in_n):
        # 입력할 단어(word), 해당 단어의 길이(len_word)
        word = sys.stdin.readline()
        len_word = len(word)

        arr_x.append((word, len_word))

    arr_y = list(set(arr_x))
    arr_y.sort(key=lambda x: (x[1], x[0]))

    for i in arr_y:
        print(i[0])


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())
    solution()
