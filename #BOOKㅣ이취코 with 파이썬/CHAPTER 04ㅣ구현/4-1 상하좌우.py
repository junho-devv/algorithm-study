def solution():
    direction = ['L', 'R', 'U', 'D']
    xDirection = [-1, 1, 0, 0]
    yDirection = [0, 0, -1, 1]

    x, y = 1, 1

    for plan in plans:
        for i in range(len(direction)):
            if plan == direction[i]:
                xTemp = x + xDirection[i]
                yTemp = y + yDirection[i]

        if xTemp < 1 or yTemp < 1 or xTemp > n or yTemp > n:
            continue

        x, y = xTemp, yTemp

    print(x, y)


if __name__ == "__main__":

    import sys

    n = int(sys.stdin.readline())
    plans = sys.stdin.readline().split()

    solution()
