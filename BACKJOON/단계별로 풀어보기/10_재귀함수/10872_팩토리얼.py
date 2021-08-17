def do_factorial(a_num):

    if a_num == 0:
        return 1

    return a_num * do_factorial(a_num - 1)


input_x = int(input())

answer = do_factorial(input_x)

print(answer)
