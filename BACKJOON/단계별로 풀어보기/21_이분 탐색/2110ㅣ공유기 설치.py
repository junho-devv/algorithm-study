# 집의 개수(h_num)와 공유기의 개수(r_num) 입력하기
h_num, r_num = map(int, input().split())
# 집의 좌표를 원소로 가지는 리스트 입력하기
h_list = []
for _ in range(h_num):
    h_list.append(int(input()))


def solution():
    answer = 0

    h_list.sort()

    min_gap = 1
    max_gap = h_list[-1] - h_list[0]

    while min_gap <= max_gap:
        # 공유기의 개수
        r_count = 1
        # 가장 인접한 두 공유기 사이의 거리(mid_gap)
        mid_gap = (max_gap + min_gap) // 2
        # h_list[0]에 공유기를 설치한 후, 다음 공유기를 설치할 위치
        r_pos = h_list[0]
        # 공유기 설치하기
        for i in range(1, h_num):
            if h_list[i] >= r_pos + mid_gap:
                r_pos = h_list[i]
                r_count += 1

        if r_count >= r_num:
            min_gap = mid_gap + 1
            answer = mid_gap
        else:
            max_gap = mid_gap - 1

    return answer


print(solution())
