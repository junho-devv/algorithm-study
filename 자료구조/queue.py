# -*- coding: euc-kr -*-

from collections import deque

# pop() ������ �ð� ���⵵�� O(N)�̱⿡ 
# ��� �ִ� �������� ������ ������ ���� �������ϴ�. 
# �ֳ��ϸ� ù ��° �����͸� ������ �Ŀ���
# �� �ڿ� �ִ� ��� �����͸� ������ �� ĭ�� ������ �ϰ�,
# �� �տ��� �����͸� �����Ϸ��� �� ���� ��� �����͸� �ڷ� �� ĭ�� �о���� �ϱ� �����Դϴ�.

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