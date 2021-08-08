import sys
import math

# 반지름 R(radius_R) 입력받기
radius_R = int(sys.stdin.readline())
# 유클리드 기하학에서 반지름이 R인 원의 넓이 출력하기
print("{0:.6f}".format(radius_R ** 2 * math.pi))
# 택시 기하학에서 반지름이 R인 원의 넓이 출력하기
print("{0:.6f}".format(radius_R ** 2 * 2))
