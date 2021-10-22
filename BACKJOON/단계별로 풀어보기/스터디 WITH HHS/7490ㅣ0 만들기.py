import sys


def choose(para_int, para_formula, para_n):
    if para_int == para_n + 1:
        temp_formula = para_formula.replace(' ', '')
        if eval(temp_formula) == 0:
            print(para_formula)
        return
    # ASCII 코드순, ' ' < '+' < '-'
    choose(para_int + 1, para_formula + ' ' + str(para_int), para_n)
    choose(para_int + 1, para_formula + '+' + str(para_int), para_n)
    choose(para_int + 1, para_formula + '-' + str(para_int), para_n)


num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    in_n = int(sys.stdin.readline())

    choose(2, "1", in_n)
    print()
