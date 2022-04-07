in_a, in_b = input().split()

in_a = list(in_a)
in_a.reverse()
in_a = int("".join(in_a))
in_b = list(in_b)
in_b.reverse()
in_b = int("".join(in_b))

answer = in_a if in_a > in_b else in_b
print(answer)
