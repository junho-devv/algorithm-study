def solution():
    # 테스트 케이스의 개수(num_t) 입력받기
    num_t = int(input())
    for _ in range(num_t):
        # 층(floor_x), 호(ho_x) 입력받기
        floor_x = int(input())
        ho_x = int(input())

        apartment_x = [[] for _ in range(floor_x + 1)]
        # 0층 i호엔 i명이 산다
        for i in range(ho_x):
            apartment_x[0].append(i + 1)

        for i in range(1, floor_x + 1):
            for j in range(ho_x):
                apartment_x[i].append(sum(apartment_x[i - 1][0: j + 1]))

        answer = apartment_x[floor_x][ho_x - 1]
        # 결과(answer) 출력하기
        print(answer)


solution()
