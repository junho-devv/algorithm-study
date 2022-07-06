class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def is_empty(self):
        return not self.items


if __name__ == "__main__":

    stk = Stack()
    print(stk)

    print(stk.is_empty())

    stk.push(2)
    stk.push(3)

    print(stk.items)
    print(stk.top())
