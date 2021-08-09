def do_fibonacci(a_num):

    if a_num == 0:
        return 0

    elif a_num == 1:
        return 1

    return do_fibonacci(a_num - 1) + do_fibonacci(a_num - 2)


input_x = int(input())

answer = do_fibonacci(input_x)

print(answer)
