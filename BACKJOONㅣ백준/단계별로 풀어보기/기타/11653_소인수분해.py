# 임의의 정수값(input_x) 입력받기
input_x = int(input())
# 소인수분해 시작값(pn_x)을 2로 초기화
pn_x = 2

while input_x != 1:

    if input_x % pn_x == 0:
        input_x = input_x // pn_x
        print(pn_x)

    else:
        pn_x += 1
