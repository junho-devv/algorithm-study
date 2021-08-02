def solution():

    num_x = int(input())
    arr_x = list(map(int, input().split()))
    # 소수(Prime Number)의 개수(num_pn)
    num_pn = 0

    for i in arr_x:
        # 약수(Divisor)의 개수
        num_div = 0
        for j in range(1, i + 1):
            # j가 i의 약수라면,
            if i % j == 0:
                # 약수의 개수(num_div) 1씩 증가
                num_div += 1
        # 약수의 개수(num_div)가 2개일 때, (1과 자기자신만을 약수로 가질 때)
        if num_div == 2:
            # 소수의 개수(num_pn) 1씩 증가
            num_pn += 1
    # 소수의 개수(num_pn) 출력하기
    print(num_pn)


solution()
