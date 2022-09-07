if __name__ == "__main__":

    stack_a = []

    stack_a.append(5)
    stack_a.append(2)
    stack_a.append(3)
    stack_a.append(7)
    stack_a.pop()
    stack_a.append(1)
    stack_a.append(4)
    stack_a.pop()

    print(stack_a)
    print(stack_a[::-1])
    