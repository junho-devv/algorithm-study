# -*- coding: euc-kr -*-

from collections import deque

# pop() 연산은 시간 복잡도는 O(N)이기에 
# 담고 있는 데이터의 개수가 많아질 수록 느려집니다. 
# 왜냐하면 첫 번째 데이터를 제거한 후에는
# 그 뒤에 있는 모든 데이터를 앞으로 한 칸식 당겨줘야 하고,
# 맨 앞에서 데이터를 삽입하려면 그 전에 모든 데이터를 뒤로 한 칸씩 밀어줘야 하기 때문입니다.

que01 = []

que01.append(2)
que01.append(3)
que01.append(4)
que01.pop(0)

print(que01)

que = deque()
print(que)

que.append(7)
que.append(9)
que.popleft()

print(que)