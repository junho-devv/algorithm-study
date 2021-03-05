n = 1260
count = 0

coin_types = [500, 100, 50, 10]
coin_numbers = [0, 0, 0, 0]

for coin in coin_types:
    count += n // coin
    n %= coin
print(count)

n =1260
count = 0

for x in range(len(coin_types)):
    coin_numbers[x] = n // coin_types[x]
    n %= coin_types[x]
    count += coin_numbers[x] 

print(coin_numbers)
print(count)

# DDDD
money = int(input("money : "))
count = 0

for coin in coin_types:
    count += money // coin
    money %= coin

print(count)