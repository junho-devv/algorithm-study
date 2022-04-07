in_a, in_b, in_c = map(int, input().split())


def power(para_a, para_b):
    if para_b == 1:
        return para_a % in_c
    else:
        temp = power(para_a, para_b // 2)
        if para_b % 2 == 0:
            return temp * temp % in_c
        else:
            return temp * temp * para_a % in_c


print(power(in_a, in_b))

