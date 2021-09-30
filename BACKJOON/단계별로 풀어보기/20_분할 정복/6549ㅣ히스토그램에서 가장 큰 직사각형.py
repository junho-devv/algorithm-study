import sys

input = sys.stdin.readline

while True:
    histogram_n = list(map(int, input().split()))

    if histogram_n[0] == 0:
        break

