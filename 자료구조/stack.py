# -*- coding: euc-kr -*-

stack = []

# append() �� pop() �Լ��� ���� stack�� ����
stack.append(5)
stack.append(2)
stack.append(7)
stack.append(1)
stack.pop()
stack.append(4)
stack.pop()
stack.append(3)

print(stack)
print(stack[::-1])