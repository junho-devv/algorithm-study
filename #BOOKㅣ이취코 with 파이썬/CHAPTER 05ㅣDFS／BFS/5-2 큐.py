if __name__ == "__main__":

    from collections import deque

    que_a = deque()

    que_a.append(5)
    que_a.append(2)
    que_a.append(3)
    que_a.append(7)
    que_a.popleft()
    que_a.append(1)
    que_a.append(4)
    que_a.popleft()

    print(que_a)
    que_a.reverse()
    print(que_a)
