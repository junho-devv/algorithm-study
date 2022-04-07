def solution():
    # 전체 사람의 수(num_p) 입력받기
    num_p = int(input())
    # 전체 사람의 몸무게와 키를 저장할 배열(arr_p)
    arr_p = []

    for _ in range(num_p):

        weight_x, height_x = map(int, input().split())

        arr_p.append([weight_x, height_x, 1])

    for a in range(num_p):
        for b in range(num_p):
            # 자기자신과 비교는 생략
            if a == b:
                continue

            if arr_p[a][0] < arr_p[b][0] and arr_p[a][1] < arr_p[b][1]:
                arr_p[a][2] += 1
    # 결과 출력하기
    for i in arr_p:
        print(i[2], end=' ')


solution()
