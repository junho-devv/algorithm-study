in_n = int(input())

count_5 = 0

while in_n != 0:

    in_n //= 5
    count_5 += in_n

print(count_5)
