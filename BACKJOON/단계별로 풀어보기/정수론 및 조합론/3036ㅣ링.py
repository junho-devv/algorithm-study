in_n = int(input())
circles = list(map(int, input().split()))


def get_gcd(para_a, para_b):
    return get_gcd(para_b, para_a % para_b) if para_b else para_a


results = []
for i in range(1, in_n):
    gcd_n = get_gcd(circles[0], circles[i])
    result = [str(circles[0] // gcd_n), str(circles[i] // gcd_n)]
    result = '/'.join(result)
    results.append(result)

for result in results:
    print(result)
