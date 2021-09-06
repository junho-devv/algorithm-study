in_n, in_k = map(int, input().split())

coins = []
for _ in range(in_n):
    coins.append(int(input()))

num_coins = 0
coin_x = coins.pop()

while in_k != 0:

    if coin_x > in_k:
        coin_x = coins.pop()
        continue

    else:
        in_k -= coin_x
        num_coins += 1

print(num_coins)
