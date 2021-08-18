def solution():
    # 좌표의 수(num_n) 입력받기
    num_n = int(input())
    # 좌표를 저장할 배열(arr_n)
    arr_n = []
    # 좌표 입력받기
    for _ in range(num_n):
        arr_n.append(list(map(int, input().split())))
    # 정렬하기
    arr_n.sort(key=lambda x: (x[0], x[1]))
    # 결과 출력하기
    for i in arr_n:
        print(i[0], i[1])


solution()
