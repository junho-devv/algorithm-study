def solution():
    answer = 0

    h_list.sort()

    min_gap = h_list[1] - h_list[0]
    max_gap = h_list[-1] - h_list[0]

    while min_gap <= max_gap:
        # 공유기의 개수
        r_count = 1

        mid_gap = (max_gap + min_gap) // 2
        # h_list[0]에 공유기를 설치한 후, 다음 공유기를 설치할 위치
        r_pos = h_list[0] + mid_gap
        # 공유기 설치하기
        answer = max_gap
        r_index = 0
        for i in range(1, h_num):
            if h_list[i] >= r_pos:
                r_pos += h_list[i] + mid_gap
                r_count += 1
                answer = min(answer, h_list[i] - h_list[r_index])
                r_index = i
        if r_count == r_num:
            break
        elif r_count < r_num:
            max_gap = mid_gap - 1
        else:
            min_gap = mid_gap + 1

    return answer


# 집의 개수(h_num)와 공유기의 개수(r_num) 입력하기
h_num, r_num = map(int, input().split())
# 집의 좌표를 원소로 가지는 리스트 입력하기
h_list = []
for _ in range(h_num):
    h_list.append(int(input()))

print(solution())
