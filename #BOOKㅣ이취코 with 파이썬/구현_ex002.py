def solution():

    a_string = sys.stdin.readline()
    b_string = ""

    a_sum = 0

    for i in range(len(a_string)):
        if a_string[i].isalpha():
            b_string += a_string[i]
        elif a_string[i].isdigit():
            a_sum += int(a_string[i])

    b_string += str(a_sum)

    print(b_string)


if __name__ == "__main__":

    import sys

    solution()
