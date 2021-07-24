def solution():
    # 고정비용(val_x), 가변비용(val_y), 제품가격(val_z)
    val_x, val_y, val_z = map(int, input().split())

    # 가변비용이 제품가격과 크거나 같다면, 손익분기점이 존재하지 않는다
    if val_y >= val_z:
        answer = -1

    else:
        answer = val_x // (val_z - val_y) + 1

    # 결과(answer) 출력하기
    print(answer)


solution()
