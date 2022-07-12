coin_num = int(input())

coin_list = list(map(int, input().split()))
coin_list.sort()

target = 1

for i in coin_list:

    if target < i:
        break

    target += i

print(target)

# 예를 들어 1, 2, 3 까지 가능하다면
# 다음 입력이 5일 때
# TARGET은 6까지 숫자를 만들 수 있고 다음 5가 들어오면
# 기존의 1부터 6까지 숫자들에 5를 더해 6부터 11까지의 합을 만들어 낼 수 있다.
