def solution():
    # 숫자 X(input_x) 입력받기
    input_x = int(input())
    ord_x = 1
    end_x = 0
    for i in range(1, input_x):
        if ord_x >= input_x:
            start_x = i
            break
        else:
            ord_x += i + 1

    if start_x % 2 == 0:
        diff_x = ord_x - start_x
        
    else:
        print()


solution()
