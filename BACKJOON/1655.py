# title : 가운데를 말해요.
num_x = int(input())
seq_x = []


def solution():

    for _ in range(num_x):
        seq_x.append(int(input()))
        seq_x.sort()

        len_x = len(seq_x) - 1
        mid_x = len_x // 2
        print(seq_x[mid_x])


solution()
