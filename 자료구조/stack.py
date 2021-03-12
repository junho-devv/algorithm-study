# -*- coding: euc-kr -*-

stack = []

# append() 와 pop() 함수를 통해 stack을 구현
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