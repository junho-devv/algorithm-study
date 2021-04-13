# 특정 거리의 도시 찾기
def solution():

    return 0


c_num, r_num, s_path, c_start = map(int, input().split())

road_list = []

for _ in range(r_num):
    road_list.append(list(map(int, input().split())))

print(road_list)
