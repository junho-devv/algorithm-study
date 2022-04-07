in_a, in_b = map(int, input().split())

# GCD(Greatest Common Divisor)
a, b = in_a, in_b
while b != 0:
    a = a % b
    a, b = b, a
gcd_ab = a
print(gcd_ab)
# LCM(Least Common Multiple)
lcm_ab = in_a * in_b // gcd_ab
print(lcm_ab)
